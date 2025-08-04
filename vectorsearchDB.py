#for importing Ollama embeddings
from langchain_ollama import OllamaEmbeddings
#for importing model that creates text and converts to vectors
from langchain_chroma import Chroma
#for creating documents for chromaDB
from langchain_core.documents import Document
import os
import pandas as pd

df=pd.read_csv('realistic_restaurant_reviews.csv')
embeddings=OllamaEmbeddings(model='mxbai-embed-large')

#check if database exists
#if it does, csv file has converted into vectors and added to the database
db_location="./chrome_langchain_db"
#else, convert and add (lines 17-30)
add_documents=not os.path.exists(db_location)

if add_documents:
    documents=[]
    ids=[]

    for i,row in df.iterrows():
        document=Document(
            page_content=row["Title"]+"..."+row["Review"],
            metadata={"rating":row["Rating"],"date":row["Date"]},
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document)

#initialize vector store if directory(db_location @line 15) already exists
vector_store=Chroma(
    collection_name="restaurant_reviews",
    persist_directory=db_location,
    embedding_function=embeddings
)

#if directory doesn't exist, then this if statement will add document data into the vector store
if add_documents:
    vector_store.add_documents(documents=documents,ids=ids)

#this retriever looks up documents, then pass into prompt for LLM
retriever=vector_store.as_retriever(
    search_kwargs={"k":5}
)