from fastmcp import FastMCP
import nautoclient

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    """
        This function can be used to greet the user with the provided name. 
    """
    return f"Hello, {name}!"

@mcp.tool
def get_devices_count() -> int:
    """
        This function will return the connected devices to thbe nautobot. 
    """
    return 5


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=8085
    )