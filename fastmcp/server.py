from fastapi import FastAPI, HTTPException

from .schemas import ToolRequest, ToolResponse
from .tools.echo_tool import run_echo_tool
from .tools.external_api_tool import run_external_api_tool


class FastMCPServer:
    def __init__(self, title: str = "FastMCP Example", version: str = "0.1.0"):
        self.app = FastAPI(title=title, version=version)
        self.tools: dict[str, dict[str, str | callable]] = {}

        self.register_tool("echo", run_echo_tool, "Echoes prompt strings back in a structured response")
        self.register_tool(
            "external_api",
            run_external_api_tool,
            "Fetch external business intelligence data from a public API",
        )

        self.app.get("/")(self.read_root)
        self.app.get("/tools")(self.list_tools)
        self.app.post("/tool/{tool_name}", response_model=ToolResponse)(self.invoke_tool)

    def read_root(self) -> dict[str, str]:
        return {
            "message": "FastMCP example server is running",
            "tool_endpoint": "/tool/{tool_name}",
            "tools": "/tools",
            "docs": "/docs",
        }

    def list_tools(self) -> dict[str, list[dict[str, str]]]:
        return {
            "tools": [
                {"name": name, "description": metadata["description"]}
                for name, metadata in self.tools.items()
            ]
        }

    def invoke_tool(self, tool_name: str, payload: ToolRequest) -> ToolResponse:
        if tool_name not in self.tools:
            raise HTTPException(status_code=404, detail=f"Tool '{tool_name}' not found")

        if not payload.prompt.strip():
            raise HTTPException(status_code=400, detail="Prompt is required")

        tool_runner = self.tools[tool_name]["runner"]
        return tool_runner(payload.prompt)

    def register_tool(self, name: str, runner: callable, description: str) -> None:
        self.tools[name] = {
            "runner": runner,
            "description": description,
        }


mcp_server = FastMCPServer()
app = mcp_server.app
