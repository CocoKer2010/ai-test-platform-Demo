import json
from ai.llm_client import call_llm

def generate_test_cases(requirement: str):
    result = call_llm(requirement)
    return json.loads(result)