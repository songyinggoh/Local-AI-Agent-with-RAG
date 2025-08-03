from tempfile import template
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model=OllamaLLM(model="mistral")

template="""
You are an expert in answering questions about a pizza restaurant.

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""

prompt=ChatPromptTemplate.from_template(template)
#invoking chain combining multiple things together to run loop
chain=prompt | model  

while True:
    print('\n\n---------------------------------------------')
    question=input("Please ask your question(press 'q' to quit):")
    if question.lower()=='q':
        break
    result=chain.invoke({"reviews":[],"question":question})
    print(result)