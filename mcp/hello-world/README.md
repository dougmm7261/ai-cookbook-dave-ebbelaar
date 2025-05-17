# Hello World MCP Server

This simple example demonstrates how to create an MCP server that replies with
`"world"` whenever the input to its tool is `"hello"`.

## Running the Server

1. Install the MCP Python SDK. From the repository root you can run:

```bash
uv pip install -r mcp/crash-course/requirements.txt
```

2. Start the server using the MCP CLI in development mode:

```bash
mcp dev server.py
```

3. In the MCP Inspector, call the `hello` tool with the argument `word="hello"`.
It will respond with `world`.

You can also run the server directly with `python server.py` and connect using
any MCP-compatible client.
