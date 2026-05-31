from pydantic import BaseModel


class EchoToolResponse(BaseModel):
    result: str


def run_echo_tool(prompt: str) -> EchoToolResponse:
    return EchoToolResponse(result=f"Echo: {prompt}")
