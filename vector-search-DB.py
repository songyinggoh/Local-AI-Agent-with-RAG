#for importing Ollama embeddings
from langchain_ollama.vectorstores import OllamaEmbeddings
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
#else, convert and add
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

vector_store=Chroma(
    collection_name="restaurant_reviews",
    persist_directory=db_location
    embedding_function=embeddings
)
if add_documents:
    vector_store.add_documents(documents=documents,ids=ids)