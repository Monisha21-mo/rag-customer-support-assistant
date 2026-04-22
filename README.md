🤖 RAG Customer Support Assistant (LangGraph + HITL)
 
 Overview

This project is a Retrieval-Augmented Generation (RAG) system designed to answer questions from PDF documents.

It processes documents, retrieves relevant content using embeddings, and generates context-aware answers. It also includes routing logic and a Human-in-the-Loop (HITL) mechanism.


🚀 Features

* 📄 PDF document processing
* 🔍 Semantic search using embeddings
* 🤖 Context-aware answer generation
* 🔀 Query routing (intent-based)
* 👨‍💻 Human-in-the-Loop (HITL) escalation
* 🔗 Graph-based workflow

🛠️ Tech Stack

* Python
* LangChain
* ChromaDB
* HuggingFace Transformers

🧠 System Architecture

User Query
   ↓
Routing Layer
   ↓
Retriever (ChromaDB)
   ↓
Answer Generation
   ↓
HITL Check
   ↓
Final Response

📁 Project Structure

src/
  ingest.py
  retriever.py
  generator.py
  router.py
  hitl.py
  graph.py

app.py
requirements.txt
file.pdf

⚙️ How to Run

pip install -r requirements.txt
python app.py

🧪 Example

Input:

What is this document about?
Output:

[GENERAL] Answer from document

📜 License

For educational use

