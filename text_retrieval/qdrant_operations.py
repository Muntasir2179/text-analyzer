import qdrant_client
from qdrant_client.http import models
from langchain.vectorstores.qdrant import Qdrant
from .embedding_model import VectorDatabase

# loading the environment variables
import os
from dotenv import load_dotenv
load_dotenv()


class QdrantVectorDatabaseOperations:
    def __init__(self):
        # creating a qdrant client
        self.client = client = qdrant_client.QdrantClient(
            url=os.getenv('QDRANT_HOST'),
            api_key=os.getenv('QDRANT_API_KEY')
        )
        # getting the collection name from the environment
        self.collection_name = os.getenv('TEXT_COLLECTION_NAME')

    # function for creating a collection
    def create_text_collection(self):
        collection_list = self.client.get_collections()
        if len(collection_list.collections) == 0:  # when there is no collection created before
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=models.VectorParams(size=768,  # embedding vector dimension
                                                distance=models.Distance.COSINE)  # distance calculation function
            )
    
    # function for deleting the collection
    def delete_collection(self):
        collection_list = self.client.get_collections()
        if len(collection_list.collections) != 0:  # when there is already a collection exists
            for i in range(len(collection_list.collections)):
                self.client.delete_collection(collection_name=collection_list.collections[i].name)
    
    # function for inserting user documents into the collection
    def insert_documents(self, documents):
        # creating a vector store object
        vector_store = None
        if vector_store is None:
            # in case we have no vector_store then we initialize and add the documents to the vector database
            vector_store = Qdrant(
                client=self.client,
                collection_name=self.collection_name,
                embeddings=VectorDatabase.get_model()  # getting the embedding model
            )
            _ = vector_store.add_documents(documents=documents)
        else:
            # in case we already have vector_store initialized then we just add the documents to the vector database
            _ = vector_store.add_documents(documents=documents)

# # creating a qdrant client
# client = qdrant_client.QdrantClient(
#     url=os.getenv('QDRANT_HOST'),
#     api_key=os.getenv('QDRANT_API_KEY')
# )

# collection_name = os.getenv('TEXT_COLLECTION_NAME')  # getting the collection name from the environment

# # function for creating a collection
# def create_text_collection():
#     collection_list = client.get_collections()
#     if len(collection_list.collections) == 0:  # when there is no collection created before
#         client.create_collection(
#             collection_name=collection_name,
#             vectors_config=models.VectorParams(size=768,  # embedding vector dimension
#                                             distance=models.Distance.COSINE)  # distance calculation function
#         )


# # function for deleting the collection
# def delete_collection():
#     collection_list = client.get_collections()
#     if len(collection_list.collections) != 0:  # when there is already a collection exists
#         for i in range(len(collection_list.collections)):
#             client.delete_collection(collection_name=collection_list.collections[i].name)


# # function for inserting user documents into the collection
# def insert_documents(documents):
#     # creating a vector store object
#     vector_store = None
#     if vector_store is None:
#         # in case we have no vector_store then we initialize and add the documents to the vector database
#         vector_store = Qdrant(
#             client=client,
#             collection_name=collection_name,
#             embeddings=VectorDatabase.get_model()  # getting the embedding model
#         )
#         _ = vector_store.add_documents(documents=documents)
#     else:
#         # in case we already have vector_store initialized then we just add the documents to the vector database
#         _ = vector_store.add_documents(documents=documents)
