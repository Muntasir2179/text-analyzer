from langchain.embeddings.huggingface import HuggingFaceEmbeddings

class VectorDatabase:
    _embedding_model = None

    @classmethod
    def load_model(self):
        if self._embedding_model is None:
            self._embedding_model = HuggingFaceEmbeddings(
                model_name= "sentence-transformers/all-MiniLM-L6-v2",  # "sentence-transformers/all-mpnet-base-v2"
                cache_folder= 'embedding_model'
            )
            print("The embedding model is loading")
    
    @classmethod
    def get_model(self):
        return self._embedding_model