# document-qa
RAG-based document Q&amp;A system built with Python, PyPDF2 and Groq API
# Document Q&A (RAG System)
Ask questions about any PDF using AI. Built with Python, PyPDF2 and Groq API.

## How it works
1. PDF is loaded and split into 500-word chunks
2. Your question is matched against all chunks using keyword search
3. Most relevant chunk is sent to AI with your question
4. AI answers based only on that chunk

## How to run
1. Install dependencies: pip install groq PyPDF2 python-dotenv
2. Add your Groq API key to .env file
3. Run: python rag_app.py
