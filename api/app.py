from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from chains.full_chain import run_full_chain

app = FastAPI(title="BBDD Chatbot API")

class QueryInput(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str

@app.post("/query", response_model=QueryResponse)
def query_db(input_data: QueryInput):
    try:
        answer = run_full_chain(input_data.question)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
