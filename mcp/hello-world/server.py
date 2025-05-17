from mcp.server.fastmcp import FastMCP

mcp = FastMCP("HelloWorld")

@mcp.tool()
def hello(word: str) -> str:
    """Return 'world' when the input word is 'hello'."""
    if word.lower().strip() == "hello":
        return "world"
    return "I only respond to 'hello'."

if __name__ == "__main__":
    mcp.run()
