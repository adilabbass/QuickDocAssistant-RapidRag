from fastapi import FastAPI, HTTPException
from app.retriever import Retriever
from app.generator import Generator

app = FastAPI()

retriever = Retriever(data_path="data/")
generator = Generator()

@app.get("/")
def read_root():
    return {"message": "Welcome to QuickRAG Q&A API"}

@app.post("/ask/")
def ask_question(query: str):
    try:
        docs = retriever.get_relevant_docs(query)
        context = "\n".join([doc.page_content for doc in docs])
        answer = generator.generate_answer(query, context)
        return {"query": query, "context": context, "answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
