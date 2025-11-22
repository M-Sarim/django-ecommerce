from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Order, OrderProduct
from products.models import Product

User = get_user_model()


class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="test@example.com",
            password="password",  # nosec: B106
        )
        self.product = Product.objects.create(
            title="Test Product", price=10.00, discounted_price=5.00
        )
        self.order_product = OrderProduct.objects.create(
            user=self.user, product=self.product, quantity=2
        )
        self.order = Order.objects.create(user=self.user)
        self.order.products.add(self.order_product)

    def test_get_total_price(self):
        # Total price should be 2 * 5.00 = 10.00 (since discounted price is used)
        self.assertEqual(self.order.get_total_price(), 10.00)


class CheckoutViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            email="test@example.com",
            password="password",  # nosec: B106
        )
        self.client.login(email="test@example.com", password="password")  # nosec: B106
        self.order = Order.objects.create(user=self.user)

    def test_checkout_view_get(self):
        response = self.client.get(reverse("order:checkout"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "checkout.html")
