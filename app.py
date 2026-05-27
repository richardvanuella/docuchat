import streamlit as st
from rag import setup_llm, proses_dokumen, tanya_dokumen

# ========== CONFIG ==========
st.set_page_config(
    page_title="DocuChat",
    page_icon="📄",
    layout="centered"
)

st.title("📄 DocuChat")
st.caption("Upload dokumen kamu, lalu tanya apapun tentangnya!")

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("⚙️ Setup")
    api_key = st.text_input("Gemini API Key", type="password")
    
    st.divider()
    
    st.header("📂 Upload Dokumen")
    uploaded_file = st.file_uploader("Upload file .txt", type=["txt"])
    
    if uploaded_file and api_key:
        with st.spinner("Memproses dokumen..."):
            teks = uploaded_file.read().decode("utf-8")
            llm = setup_llm(api_key)
            collection, jumlah = proses_dokumen(teks)
            
            st.session_state.collection = collection
            st.session_state.llm = llm
            st.session_state.siap = True
            
        st.success(f"✅ Dokumen siap! ({jumlah} potongan)")

# ========== CHAT ==========
if "messages" not in st.session_state:
    st.session_state.messages = []

# Tampilkan history chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input pertanyaan
if pertanyaan := st.chat_input("Tanya sesuatu tentang dokumen..."):
    if not st.session_state.get("siap"):
        st.error("⚠️ Upload dokumen dan masukkan API key dulu!")
    else:
        # Tampilkan pertanyaan user
        st.session_state.messages.append({"role": "user", "content": pertanyaan})
        with st.chat_message("user"):
            st.write(pertanyaan)
        
        # Jawaban AI
        with st.chat_message("assistant"):
            with st.spinner("Mencari jawaban..."):
                jawaban, sumber = tanya_dokumen(
                    pertanyaan,
                    st.session_state.collection,
                    st.session_state.llm
                )
            
            st.write(jawaban)
            
            # Tampilkan sumber
            with st.expander("📚 Sumber dari dokumen"):
                for i, s in enumerate(sumber):
                    st.caption(f"Potongan {i+1}: {s[:200]}...")
        
        st.session_state.messages.append({"role": "assistant", "content": jawaban})