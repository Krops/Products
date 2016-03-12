# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse


class ProductsTestCase(TestCase):
    fixtures = ['test_data.json']

    def test_last_without_auth(self):
        "Test last page without authorization"
        response = self.client.get(reverse('last'))
        self.assertEqual(None, response.context)

    def test_last_with_auth(self):
        "Test last page with authorization"
        self.client.post(
            reverse('login'), {'username': 'admin', 'password': '110692'})
        response = self.client.get(reverse('last'))
        self.assertContains(response, 'Product2')
        self.assertContains(response, 'Hello world2!!!')
        self.assertNotContains(response, 'Product_NOT')

    def test_category(self):
        "Test category page"
        response = self.client.get(reverse('category', args=['category2']))
        self.assertContains(response, 'Hello category2')
        self.assertContains(response, 'Product2')
        self.assertNotContains(response, 'Product_NOT')
