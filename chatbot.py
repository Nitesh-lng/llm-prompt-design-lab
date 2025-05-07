from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage , AIMessage
import os 

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

model=ChatGroq(
    model="meta-llama/llama-4-scout-17b-16e-instruct"
)
chat=[
    SystemMessage(
        content="You are a helpful assistant that provides detailed explanations of research papers. You can also provide code snippets and mathematical details if needed."
    )
]
while True:
    user_input=input("Enter your query here:")
    chat.append(
        HumanMessage(
            content=user_input
        )
    )
    if user_input=="exit":
        break
    else:
        response=model.invoke(chat)
        chat.append(
            AIMessage(
                content=response.content
            )
        )
        print(response.content)
print("Chat history:",chat)