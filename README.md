# FastMCP Example

A minimal Python FastMCP-style server with a single tool endpoint and Playwright Page Object Model (POM) tests.

## Project structure

- `fastmcp/` - package implementing the FastMCP server and tool registry
- `fastmcp/tools/` - individual tool implementations
- `tests/` - unit tests, browser tests, and BDD scenarios
- `tests/pages/` - Playwright page object classes
- `tests/features/` - BDD feature files
- `tests/steps/` - BDD step definitions
- `tests/utils/` - shared browser and server helpers
- `fastmcp/tools/external_api_tool.py` - example business intelligence tool using an external API

## Setup

1. Install Python 3.10+ and ensure it is on your PATH.
2. Install the Allure CLI separately so you can view test reports.
3. From the project root:

```bash
python -m pip install --upgrade pip
python -m pip install -e .[dev]
python -m playwright install chromium
```

## Run the server

```bash
python server.py
```

Open `http://127.0.0.1:8000` to verify the serve running.

## FastMCP endpoints

- `GET /` - server status
- `GET /tools` - registered tool metadata
- `POST /tool/{tool_name}` - invoke a tool

The new `external_api` tool can be called at `/tool/external_api` and returns a simple business intelligence summary from a public API.

Example request:

```bash
curl -X POST http://127.0.0.1:8000/tool/echo \
  -H "Content-Type: application/json" \
  -d '{"prompt":"hello"}'
```

## Tests

Run the existing pytest suite:

```bash
pytest
```

Generate Allure results:

```bash
pytest --alluredir=allure-results
```

View the report locally after installing the Allure CLI:

```bash
allure serve allure-results
```

Or generate a static HTML report:

```bash
allure generate allure-results --clean -o allure-report
allure open allure-report
```

## Page Object Model

The browser tests use a dedicated POM class at `tests/pages/root_page.py`.
That keeps UI interactions separate from test assertions and makes the suite easier to extend.
