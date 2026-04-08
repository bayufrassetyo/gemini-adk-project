from fastapi import FastAPI
from pydantic import BaseModel
from agent import classify_issue

# 🔥 IMPORT BARU (Track 3)
from database import init_db, run_query
from ai_sql import generate_sql

app = FastAPI()

# 🔹 Existing (Track 1 & 2)
class Request(BaseModel):
    text: str

# 🔥 BARU (Track 3)
class QueryRequest(BaseModel):
    query: str

# 🔥 INIT DATABASE (Track 3)
init_db()

@app.get("/")
def root():
    return {"message": "AI System is running 🚀"}

# 🔹 Track 1 & 2
@app.post("/classify")
def classify(req: Request):
    try:
        result = classify_issue(req.text)
        return result
    except Exception as e:
        return {
            "error": "Internal error",
            "details": str(e)
        }

# 🔥 Track 3 (BARU)
@app.post("/query")
def query_db(req: QueryRequest):
    try:
        sql = generate_sql(req.query)
        result = run_query(sql)

        return {
            "input": req.query,
            "generated_sql": sql,
            "result": result
        }

    except Exception as e:
        return {
            "error": "Query failed",
            "details": str(e)
        }