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
    tools=[search]
)

pipeline = prompt | agent

try: 
    response = pipeline.invoke({})
    text = response.content
    clean_text = text.encode('utf-8').decode('unicode_escape')
    print(clean_text)

except RateLimitError:
    print("No Tokens/Too much load on the OpenAPI")
except Exception as e:
    print(e)
