from langchain_groq import ChatGroq

llm = ChatGroq(
    groq_api_key='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',
    model_name = "llama-3.1-70b-versatile",
    temperature=0
)

response = llm.invoke('Who is Lupita Nyongo')
print (response)