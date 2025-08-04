from langchain_ollama import ChatOllama
from langchain.chains import RetrievalQA

def get_qa_chain(retriever):
    """
    Initializes the QA chain for querying the vector store.
    """
    chat = ChatOllama(
        model='llama3.2:1b',
        temperature=0.0
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=chat,
        chain_type="stuff",
        retriever=retriever
    )

    return qa_chain
