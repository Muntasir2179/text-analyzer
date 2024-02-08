from django.apps import AppConfig
from text_retrieval.embedding_model import VectorDatabase


class TextRetrievalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'text_retrieval'

    def ready(self):
        VectorDatabase.load_model()