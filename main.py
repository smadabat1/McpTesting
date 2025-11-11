from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.prompts.chat import ChatPromptTemplate
from prompts import sytemprompt
from openai import RateLimitError

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
def search(query: str) -> str:
    """Search for information."""
    return f"Results for: {query}"


agent = create_agent(
    model=llm,
    tools=[search],
    system_prompt=sytemprompt.prompt
)


try: 
    result = agent.invoke({"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]})
    print(result)

except RateLimitError:
    print("No Tokens/Too much load on the OpenAPI")
except Exception as e:
    print(e)
