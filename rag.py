import google.generativeai as genai
import chromadb
from sentence_transformers import SentenceTransformer

# ========== SETUP ==========
embedder = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.Client()

def setup_llm(api_key):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        system_instruction="""
        Kamu adalah asisten yang membantu menjawab pertanyaan berdasarkan dokumen.
        Aturan:
        - Jawab HANYA berdasarkan dokumen yang diberikan
        - Kalau jawabannya tidak ada di dokumen, bilang "Informasi tidak tersedia di dokumen."
        - Jawab dalam Bahasa Indonesia
        - Jawaban singkat, padat, dan jelas
        """
    )

# ========== PROSES DOKUMEN ==========
def proses_dokumen(teks, nama_collection="dokumen"):
    # Hapus collection lama kalau ada
    try:
        client.delete_collection(nama_collection)
    except:
        pass
    
    collection = client.create_collection(nama_collection)
    
    # Pecah dokumen jadi potongan 500 karakter
    potongan = []
    ukuran = 500
    overlap = 50
    
    for i in range(0, len(teks), ukuran - overlap):
        potongan.append(teks[i:i + ukuran])
    
    # Masukin ke database
    for i, p in enumerate(potongan):
        vector = embedder.encode(p).tolist()
        collection.add(
            documents=[p],
            embeddings=[vector],
            ids=[f"chunk_{i}"]
        )
    
    return collection, len(potongan)

# ========== TANYA DOKUMEN ==========
def tanya_dokumen(pertanyaan, collection, llm):
    # Cari potongan yang relevan
    vector_pertanyaan = embedder.encode(pertanyaan).tolist()
    hasil = collection.query(
        query_embeddings=[vector_pertanyaan],
        n_results=3
    )
    
    konteks = "\n\n".join(hasil["documents"][0])
    
    prompt = f"""
    Konteks dari dokumen:
    {konteks}
    
    Pertanyaan: {pertanyaan}
    """
    
    response = llm.generate_content(prompt)
    return response.text, hasil["documents"][0]