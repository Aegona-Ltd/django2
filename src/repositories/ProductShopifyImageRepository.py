from .BaseRepository import BaseRepository
from src.models import ProductShopifyImage


class ProductShopifyImageRepository(BaseRepository):
    def __init__(self):
        self.model = ProductShopifyImage