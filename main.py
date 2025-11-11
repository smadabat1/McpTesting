from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool
import asyncio 
from langchain_core.prompts.chat import ChatPromptTemplate
from prompts import sytemprompt
from openai import RateLimitError
from fastmcp import Client

client = Client("http://0.0.0.0:8085/mcp")

llm = ChatOpenAI(
    model="local-llama",
    base_url="http://localhost:10000/v1",
    api_key="superpassword"
)

prompt = ChatPromptTemplate([
    ("system", sytemprompt.prompt),
    ("user", "Search and Explain what LangChain is in one line")
])

@tool
async def get_connected_devices_count(query: str) -> str:
    """This function will return the number of the connected devices to the nautobot."""
    async with client:
        result = await client.call_tool("get_devices_count")
        
        return result


agent = create_agent(
    model=llm,
    tools=[get_connected_devices_count],
    system_prompt=sytemprompt.prompt
)

async def main():
    try: 
        result = await agent.ainvoke({"messages": [{"role": "user", "content": "search and let me know the count of the devices connected to nautobot?"}]})
        if isinstance(result, dict):
            messages = result.get("messages", [])
            if messages:
                final_message = messages[-1]
                print("🧠 Final Response:", final_message.content)
            else:
                print("No messages in result:", result)
        else:
            print("🧠 Final Response:", result.content)
        print("\n\n")
        print(result)

    except RateLimitError:
        print("No Tokens/Too much load on the OpenAPI")
    except Exception as e:
        print(e)

asyncio.run(main())