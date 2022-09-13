from .BaseRepository import BaseRepository
from src.models import ProductShopifyVariant


class ProductShopifyVariantRepository(BaseRepository):
    def __init__(self):
        self.model = ProductShopifyVariant