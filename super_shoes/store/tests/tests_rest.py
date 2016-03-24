from django.test import TestCase
from store.models import Store
from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User


class AccountTests(APITestCase, TestCase):
    def setUp(self):
        Store.objects.create(name="abc", address="lalalal")
        Store.objects.create(name="addres", address="lelele")
        User.objects.create_superuser('my_user', 'myemail@test.com', "my_password")

    def test_create_store_not_authorized(self):
        """
        Ensure we can create a new object.
        """
        url = reverse('store-list')
        data = {'name': 'test', "address": "lalalal"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.data["error_code"], 401)

    def test_get_not_authorized(self):
        response = self.client.get(reverse('store-list'))
        self.assertEqual(response.data["error_code"], 401)

    def test_create_store_authorized(self):
        """
        Ensure we can create a new object.
        """
        url = reverse('store-list')
        data = {'name': 'test', "address": "lalalal"}
        client = APIClient()
        client.login(username='my_user', password='my_password')
        response = client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Store.objects.count(), 3)
        self.assertEqual(Store.objects.get(name="test").name, 'test')

    def test_get_authorized(self):
        client = APIClient()
        client.login(username='my_user', password='my_password')
        response = client.get(reverse('store-list'))
        self.assertEqual(response.data["success"], True)
        self.assertEqual(response.data["total_elements"], 2)
