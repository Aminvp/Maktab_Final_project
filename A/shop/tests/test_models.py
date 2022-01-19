from django.test import TestCase
from shop.models import Product, Category, Store
from accounts.models import User


class TestModel(TestCase):
    def setUp(self):
        user = User.objects.create_user(email='jack@gmail.com', full_name='jack stallone', password='12345')
        store = Store.objects.create(name='digikala', user=user)
        self.category = Category.objects.create(name='mobile')
        # self.product = Product.objects.create(
        #     category=self.category,
        #     name='this is test product',
        #     description='this is test product description',
        #     price=235000,
        #     store=store
        # )

    # def test_product_create(self):
    #     self.assertEqual(self.product.slug, 'this-is-test-product')

    def test_category_create(self):
        self.assertEqual(self.category.slug, 'mobile')


