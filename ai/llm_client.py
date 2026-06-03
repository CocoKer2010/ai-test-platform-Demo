def call_llm(prompt: str) -> str:
    return """
    [
        {
            "name": "Demo Test",
            "method": "GET",
            "url": "https://httpbin.org/get",
            "input": {},
            "expected_status": 200
        }
    ]
    """