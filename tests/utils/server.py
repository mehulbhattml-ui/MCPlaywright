import threading
import time

import httpx
import uvicorn

from fastmcp import app


class FastMCPServer:
    def __init__(self, host: str = "0.0.0.0", port: int = 8001):
        self.host = host
        self.port = port
        self.config = uvicorn.Config(app, host=self.host, port=self.port, log_level="warning", lifespan="off")
        self.server = uvicorn.Server(self.config)
        self.thread = threading.Thread(target=self.server.run, daemon=True)

    def start(self, timeout: float = 10.0) -> None:
        self.thread.start()
        # Use localhost for health check regardless of binding address
        url = f"http://localhost:{self.port}"
        deadline = time.time() + timeout

        while time.time() < deadline:
            try:
                response = httpx.get(url, timeout=1.0)
                if response.status_code == 200:
                    return
            except Exception:
                time.sleep(0.1)

        raise RuntimeError("FastMCP server did not start in time")

    def stop(self) -> None:
        self.server.should_exit = True
        self.thread.join(timeout=5)
