from ..schemas import ToolResponse


def run_echo_tool(prompt: str) -> ToolResponse:
    return ToolResponse(result=f"Echo: {prompt}")
