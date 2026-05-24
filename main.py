from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai

# Setting up the AI
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.5-flash')

app = FastAPI()

# Allowing the frontend to talk to the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    sql_query: str

@app.post("/optimize")
async def optimize_query(request: QueryRequest):
    prompt = f"""
    You are an expert Database Administrator. Analyze the following SQL query.
    1. Identify any performance bottlenecks.
    2. Provide an optimized version of the query.
    3. Give a brief, bulleted explanation of why the new query is better.
    
    Original Query:
    {request.sql_query}
    """
    
    response = model.generate_content(prompt)
    return {"optimized_result": response.text}

# Run this using: uvicorn main:app --reload