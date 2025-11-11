from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="local-llama",
    base_url="http://localhost:10000/v1",
    api_key="superpassword"
)

response = llm.invoke("Explain what LangChain is in one line.")
print(response.content)
