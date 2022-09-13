from django.contrib.auth.models import User
from src.repositories import ProductCategoryRepository,ProductRepository


def seed():
    productRepository = ProductRepository()
    productRepository.deleteAll()
    productCategoryRepository = ProductCategoryRepository()
    productCategoryRepository.deleteAll()

    model = productCategoryRepository.getModel()

    productCategoryRepository.bulkCreate(
        [
            model(id=1,name="Áo"),
            model(id=2,name="Quần"),
        ]
    )
