from pydantic import BaseModel


class ToolRequest(BaseModel):
    prompt: str


class ToolResponse(BaseModel):
    result: str
