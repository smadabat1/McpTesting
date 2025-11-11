from langchain_openai import ChatOpenAI
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
    ("user", "Explain what LangChain is in one line.")
])

pipeline = prompt | llm

try: 
    response = pipeline.invoke({})
    text = response.content
    clean_text = text.encode('utf-8').decode('unicode_escape')
    print(clean_text)

except RateLimitError:
    print("No Tokens/Too much load on the OpenAPI")
except Exception as e:
    print(e)
