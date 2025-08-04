import os
import time
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

def get_vectordb_retriever(documents):
  """
  Initializes the retriever for querying the vector store.
  """  
  embeddings = OllamaEmbeddings(model="all-minilm")

  print(f"Processing {len(documents)} document chunks...")
  start_time = time.time()

  chroma_db_path = "../models/chroma_db"
  if os.path.exists(chroma_db_path):
      print("Loading existing vector store...")
      vectorstore = Chroma(
          persist_directory=chroma_db_path,
          embedding_function=embeddings
      )
  else:
      print("Creating new vector store...")
      vectorstore = Chroma.from_documents(
          documents=documents,
          embedding=embeddings,
          persist_directory=chroma_db_path
      )

  end_time = time.time()
  print(f"Vector store operation took {end_time - start_time:.2f} seconds")

  return vectorstore.as_retriever(search_kwargs={"k": 3})