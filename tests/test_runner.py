from services.executor import run_test_case

def test_api():
    case = {
        "name": "test httpbin",
        "url": "https://httpbin.org/get",
        "method": "GET",
        "expected_status": 200
    }

    result = run_test_case(case)

    assert result["passed"]