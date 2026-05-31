import httpx

from ..schemas import ToolResponse


def run_external_api_tool(prompt: str) -> ToolResponse:
    query = prompt.strip() or "analytics"
    response = httpx.get("https://api.agify.io", params={"name": query}, timeout=10.0)
    data = response.json()
    result = (
        f"BI summary for {query}: age={data.get('age')}, count={data.get('count')}, "
        f"country_id={data.get('country_id')}"
    )
    return ToolResponse(result=result)
