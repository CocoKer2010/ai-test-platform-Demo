from fastapi import FastAPI
from ai.case_generator import generate_test_cases
from ai.data_generator import generate_test_data
from services.executor import run_test_case

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI Testing Platform Running"}

@app.post("/generate_cases")
def gen_cases(requirement: str):
    return {"cases": generate_test_cases(requirement)}

@app.post("/generate_data")
def gen_data(context: str):
    return {"data": generate_test_data(context)}

@app.post("/run_test")
def run_test(case: dict):
    return run_test_case(case)