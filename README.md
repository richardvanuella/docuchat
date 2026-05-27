# 📄 DocuChat — AI-Powered Document Chatbot

DocuChat is an AI chatbot that can answer questions based on your own documents. Upload any `.txt` file, and ask anything about its contents — powered by RAG (Retrieval-Augmented Generation).

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red?style=flat-square&logo=streamlit)
![Google Gemini](https://img.shields.io/badge/Gemini-API-orange?style=flat-square&logo=google)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_DB-green?style=flat-square)

---

## ✨ Features

- 📂 **Upload any `.txt` document** — company policies, research papers, meeting notes, etc.
- 🔍 **Semantic search** — finds relevant sections using vector similarity, not just keyword matching
- 🤖 **Grounded answers** — AI only answers based on your document, never hallucinates
- 💬 **Chat history** — keeps track of your conversation in the session
- 📚 **Source transparency** — shows which part of the document was used to answer

---

## 🏗️ How It Works

```
User Question
      ↓
Convert to vector (embedding)
      ↓
Search ChromaDB for similar document chunks
      ↓
Send top 3 relevant chunks + question to Gemini
      ↓
AI answers based only on the retrieved context
```

This is the **RAG (Retrieval-Augmented Generation)** pattern — the standard architecture used in production AI applications to ground LLM responses in real data.

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| LLM | Google Gemini 1.5 Flash |
| Vector Database | ChromaDB |
| Embeddings | Sentence Transformers (`all-MiniLM-L6-v2`) |
| UI | Streamlit |
| Language | Python 3.10+ |

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/docuchat.git
cd docuchat
```

### 2. Create and activate virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Get a Gemini API Key
- Go to [Google AI Studio](https://aistudio.google.com)
- Click **"Get API Key"** — it's free

### 5. Run the app
```bash
streamlit run app.py
```

### 6. Use it
1. Enter your Gemini API key in the sidebar
2. Upload a `.txt` file
3. Ask anything about the document!

---

## 📁 Project Structure

```
docuchat/
├── app.py              # Streamlit UI and chat logic
├── rag.py              # RAG pipeline (embedding, vector search, LLM)
├── requirements.txt    # Python dependencies
└── README.md
```

---

## 💡 Example Use Cases

- **HR Chatbot** — upload company policy docs, let employees ask questions
- **Study Assistant** — upload lecture notes, ask for explanations
- **Legal Assistant** — upload contracts, query specific clauses
- **Customer Support** — upload product documentation, answer customer queries

---

## 🔮 Future Improvements

- [ ] Support PDF and DOCX file formats
- [ ] Multi-document support
- [ ] Persistent vector database (currently resets on reload)
- [ ] Deploy to Streamlit Cloud

---

## 📜 License

MIT License — free to use and modify.
