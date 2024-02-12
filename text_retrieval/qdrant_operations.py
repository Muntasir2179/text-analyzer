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
        # getting values from environment variables
        if 'WEBSITE_HOSTNAME' not in os.environ:
            host = os.getenv('QDRANT_HOST')
            api_key = os.getenv('QDRANT_API_KEY')
            self.collection_name = os.getenv('TEXT_COLLECTION_NAME')
        else:
            # when deployed in cloud
            host = os.environ['QDRANT_HOST']
            api_key = os.environ['QDRANT_API_KEY']
            self.collection_name = os.environ['TEXT_COLLECTION_NAME']
        
        # creating a qdrant client
        self.client = qdrant_client.QdrantClient(
            url=host,
            api_key=api_key
        )        

        # creating a vector store
        self.vector_store = Qdrant(
            client=self.client,
            collection_name=self.collection_name,
            embeddings=VectorDatabase.get_model()  # getting the embedding model
        )

    # function for creating a collection
    def create_text_collection(self):
        collection_list = self.client.get_collections()
        if len(collection_list.collections) == 0:  # when there is no collection created before
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=models.VectorParams(size=384,  # embedding vector dimension
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
        # add the documents to the vector database
        _ = self.vector_store.add_documents(documents=documents)

    # function for similarity search
    def query(self, query=None):
        if query is not None:
            results = self.vector_store.similarity_search(query=query, k=2)
            return [doc.page_content for doc in results]
        else:
            return None