import os
from dotenv import load_dotenv
from groq import Groq
import PyPDF2

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def read_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def chunk_text(text, chunk_size=500):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)
    return chunks

def find_relevant_chunk(question, chunks):
    question_words = set(question.lower().split())
    best_chunk = ""
    best_score = 0
    for chunk in chunks:
        chunk_words = set(chunk.lower().split())
        score = len(question_words & chunk_words)
        if score > best_score:
            best_score = score
            best_chunk = chunk
    return best_chunk

def ask_question(relevant_chunk, question):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": f"Answer based on this context only:\n\n{relevant_chunk}"},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

pdf_path = input("Enter PDF file path: ")
print("Reading PDF...")
pdf_text = read_pdf(pdf_path)
chunks = chunk_text(pdf_text)
print(f"Done! PDF split into {len(chunks)} chunks. Ask your questions.")

while True:
    question = input("\nYour question: ")
    relevant_chunk = find_relevant_chunk(question, chunks)
    answer = ask_question(relevant_chunk, question)
    print(answer)