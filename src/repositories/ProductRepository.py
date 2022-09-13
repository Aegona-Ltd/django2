from .BaseRepository import BaseRepository
from src.models import Product


class ProductRepository(BaseRepository):
    def __init__(self):
        self.model = Product