from fastmcp import FastMCP
import nautoclient
from typing import List

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    """
        This function can be used to greet the user with the provided name. 
    """
    return f"Hello, {name}!"

@mcp.tool
def get_devices_names() -> List[str]:
    """
        This function will return the connected devices names. 
    """
    names = []
    devices = nautoclient.nautobot.dcim.devices.all()
    if(len(devices)) > 10:
        #return the names of the top 10 devices. 
        for i in range(0, 10):
            names.append(devices[i].name)
    else:
        for d in devices:
            names.append(d.name)
    return names

@mcp.tool
def get_devices_count() -> int:
    """
        This function will return the connected devices to thbe nautobot. 
    """
    devices = nautoclient.nautobot.dcim.devices.all()
    print("length of the devices - ", len(devices))
    return len(devices)


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=8085
    )