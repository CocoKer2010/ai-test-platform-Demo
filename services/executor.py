import requests

def run_test_case(case):
    res = requests.get(case["url"])

    return {
        "name": case["name"],
        "status_code": res.status_code,
        "passed": res.status_code == case["expected_status"]
    }