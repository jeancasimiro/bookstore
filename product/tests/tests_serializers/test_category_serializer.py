from django.test import TestCase

from product.factories import CategoryFactory, ProductFactory
from product.serializers import CategorySerializer


class TestCategorySerializer(TestCase):
    def setUp(self) -> None:
        self.category = CategoryFactory(title="food")
        self.category_serializer = CategorySerializer(self.category)

    def test_category_serializer(self):
        serializer_data = self.category_serializer.data
        self.assertEquals(serializer_data["title"], "food")

    def test_category_serializer_fields(self):
        expected_fields = ["title", "slug", "description", "active"]
        serializer_data = self.category_serializer.data
        for field in expected_fields:
            self.assertIn(field, serializer_data)