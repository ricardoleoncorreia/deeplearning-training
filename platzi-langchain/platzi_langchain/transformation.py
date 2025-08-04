from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_documents(docs):
    """
    Splits the loaded machine learning papers into smaller chunks for better processing.
    """
    # Initialize the text splitter with specified chunk size and overlap
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=200,
        length_function=len
    )

    # Split the documents into smaller chunks
    documents = text_splitter.split_documents(docs)

    return documents
