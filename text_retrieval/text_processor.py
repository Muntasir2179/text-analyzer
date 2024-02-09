from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


def get_document_chunks():
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n",],
        chunk_size=300,
        chunk_overlap=90,
        length_function=len
    )

    # loading all documents at once
    loader = DirectoryLoader(path='uploads', glob="**/*.txt")
    documents = loader.load()

    chunks = text_splitter.split_documents(documents=documents)

    return chunks