from fastapi.testclient import TestClient

from main import api




client = TestClient(api)



def test_root():
    URLs = [
        {
            "url" : "https://ku.bz/XbpB666ql",
            "description" : "Check redirection to the final URL",
            "expected_result" : "",
            "expected_status" : 200
        },
        {
            "url" : "invalid-url",
            "description" : "Check invalid URL format",
            "expected_result" : "",
            "expected_status" : 422
        }
    ]

    for url in URLs:
        response = client.post("/", json={"url": url['url']})
        assert response.status_code == url['expected_status']
