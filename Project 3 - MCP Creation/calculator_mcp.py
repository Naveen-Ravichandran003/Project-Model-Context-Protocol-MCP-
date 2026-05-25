from fastmcp import FastMCP

#Create MCP Server
mcp = FastMCP("Caluclator MCP")

# Tool 1  - Addition
@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers"""
    return a+b  

# Tool 2  - Sub
@mcp.tool()
def sub_numbers(a: int, b: int) -> int:
    """Sub two numbers"""
    return a-b

# Tool 3  - Multiply
@mcp.tool()
def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a*b

# Tool 4  - Divide
@mcp.tool()
def divide_numbers(a: int, b: int) -> float:
    """Divide two numbers"""
    if b==0:
        return "Cannot divide by Zero"
    return a/b

#Run MCP Server
if __name__ == "__main__":
     mcp.run() 