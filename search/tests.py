"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client


class ResponseTest(TestCase):
    def test_basic_addition(self):
        c = Client()
        response = c.post('/search/',{'query' : 'something'})
        self.assertEqual(response.status_code, 200)
