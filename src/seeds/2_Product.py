from django.contrib.auth.models import User
from src.repositories import ProductRepository


def seed():
    productRepository = ProductRepository()
    productRepository.deleteAll()

    model = productRepository.getModel()

    productRepository.bulkCreate(
        [
            model(
                product_category_id=1,
                name="Áo khoác Adidas",
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris gravida ornare erat, sed bibendum enim dapibus quis. Aenean accumsan luctus odio non semper. ",
                price=300000,
            ),
            model(
                product_category_id=1,
                name="Áo thun nike",
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris gravida ornare erat, sed bibendum enim dapibus quis. Aenean accumsan luctus odio non semper. ",
                price=400000,
            ),
            model(
                product_category_id=1,
                name="Áo sơ mi KH",
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris gravida ornare erat, sed bibendum enim dapibus quis. Aenean accumsan luctus odio non semper. ",
                price=500000,
            ),
            model(
                product_category_id=1,
                name="Áo thể thao Kuma",
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris gravida ornare erat, sed bibendum enim dapibus quis. Aenean accumsan luctus odio non semper. ",
                price=600000,
            ),
            model(
                product_category_id=2,
                name="Quần jean Adidas",
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris gravida ornare erat, sed bibendum enim dapibus quis. Aenean accumsan luctus odio non semper. ",
                price=500000,
            ),
            model(
                product_category_id=2,
                name="Quần kaki nike",
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris gravida ornare erat, sed bibendum enim dapibus quis. Aenean accumsan luctus odio non semper. ",
                price=600000,
            ),
            model(
                product_category_id=2,
                name="Quần tây",
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris gravida ornare erat, sed bibendum enim dapibus quis. Aenean accumsan luctus odio non semper. ",
                price=700000,
            ),
            model(
                product_category_id=2,
                name="Quần short",
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris gravida ornare erat, sed bibendum enim dapibus quis. Aenean accumsan luctus odio non semper. ",
                price=800000,
            ),
        ]
    )
