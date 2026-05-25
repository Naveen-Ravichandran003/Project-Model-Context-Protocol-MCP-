from mcp.server.fastmcp import FastMCP

# Create MCP Server
mcp = FastMCP("File Reader MCP")


# Tool - Read File
@mcp.tool()
def read_file(file_path: str) -> str:
    """Read file content"""

    try:
        with open(file_path, "r") as file:
            content = file.read()

        return content

    except Exception as e:
        return f"Error: {str(e)}"


# Run MCP Server
if __name__ == "__main__":
    mcp.run()