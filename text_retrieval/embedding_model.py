# vector database packages
import torch
import qdrant_client
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer
from langchain.vectorstores.qdrant import Qdrant

# for accessing environment variables
import os
from dotenv import load_dotenv
load_dotenv()

class VectorDatabase:
    _embedding_model = None

    @classmethod
    def load_model(self):
        if self._embedding_model is None:
            self._embedding_model = HuggingFaceEmbeddings(
                model_name="sentence-transformers/all-mpnet-base-v2", 
                cache_folder= 'embedding_model'
            )
            print("The embedding model is loading")
    
    @classmethod
    def get_model(self):
        return self._embedding_model