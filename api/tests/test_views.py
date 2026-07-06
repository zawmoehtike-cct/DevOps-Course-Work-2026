from api.models import Book
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class BookViewTest(APITestCase):
    def test_response_is_correct(self):
        book = Book.objects.create(
            title="Test Book", 
            author="Test Author", 
            description="Test Description"
        )

        url = reverse('api:books')

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(response.data['books'][0]['title'], 'Test Book')
