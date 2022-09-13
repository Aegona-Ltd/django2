from .BaseRepository import BaseRepository
from src.models import ProductCategory


class ProductCategoryRepository(BaseRepository):
    def __init__(self):
        self.model = ProductCategory

    def getAllActiveWithRelated(self):
        return (
            self.model.objects.prefetch_related("product_set").order_by("-id").filter()
        )
