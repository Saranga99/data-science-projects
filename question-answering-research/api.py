from fastapi import FastAPI
from src.qa_pipeline import QAPipeline


app = FastAPI()
qa=QAPipeline()

@app.get("/")
def root():
    return "QA Pipeline is Started"

@app.post("/questionContent")
async def query_content(question:str="How do I toilet train my child as he keeps wetting himself?"):
    return qa.get_content(question)

@app.post("/questionAnswering")
async def get_answers(question:str="My child has a hard time drinking from the bottle, what can I do?"):
    return qa.get_answers(question)