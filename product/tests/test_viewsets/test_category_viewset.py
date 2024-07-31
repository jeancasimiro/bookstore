import json

from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from product.factories import CategoryFactory
from product.models import Category

class CategoryViewSetTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = CategoryFactory(title="books")

    def test_get_all_category(self):
        response = self.client.get(reverse("category-list", kwargs={"version": "v1"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        category_data = json.loads(response.content)

        # Verifique a chave 'results' e a lista dentro dela
        self.assertIn("results", category_data, "Key 'results' not found in response")
        self.assertGreater(len(category_data["results"]), 0, "No categories found in 'results'")
        self.assertEqual(category_data["results"][0]["title"], self.category.title)

    def test_create_category(self):
        data = json.dumps({"title": "technology"})

        response = self.client.post(
            reverse("category-list", kwargs={"version": "v1"}),
            data=data,
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_category = Category.objects.get(title="technology")
        self.assertEqual(created_category.title, "technology")