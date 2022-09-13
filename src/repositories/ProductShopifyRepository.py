from .BaseRepository import BaseRepository
from src.models import ProductShopify


class ProductShopifyRepository(BaseRepository):
    def __init__(self):
        self.model = ProductShopify
