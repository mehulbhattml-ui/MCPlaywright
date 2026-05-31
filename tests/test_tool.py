from fastapi.testclient import TestClient

from fastmcp import app


client = TestClient(app)


def test_echo_tool_endpoint():
    response = client.post("/tool/echo", json={"prompt": "hello world"})

    assert response.status_code == 200
    assert response.json() == {"result": "Echo: hello world"}


def test_echo_tool_requires_prompt():
    response = client.post("/tool/echo", json={"prompt": "   "})

    assert response.status_code == 400
    assert response.json()["detail"] == "Prompt is required"


def test_external_api_tool_endpoint(monkeypatch):
    from fastmcp.tools import external_api_tool

    class DummyResponse:
        def __init__(self, data):
            self._data = data

        def json(self):
            return self._data

    def fake_get(url, params, timeout):
        return DummyResponse({"age": 34, "count": 257, "country_id": "US"})

    monkeypatch.setattr(external_api_tool.httpx, "get", fake_get)

    response = client.post("/tool/external_api", json={"prompt": "M."})

    assert response.status_code == 200
    assert "BI summary for M." in response.json()["result"]
