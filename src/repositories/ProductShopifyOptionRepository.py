from .BaseRepository import BaseRepository
from src.models import ProductShopifyOption


class ProductShopifyOptionRepository(BaseRepository):
    def __init__(self):
        self.model = ProductShopifyOption