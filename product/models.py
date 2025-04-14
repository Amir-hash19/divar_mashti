from django.db import models
from account.models import UserAccount
from decimal import Decimal



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120,unique=True)

    def __str__(self):
        return self.name




class Product(models.Model):

    PUBLISH_STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('publish', 'Published'),
    ]

    PRODUCT_STATUS_CHOICES = [
        ('available', 'Available'),  # موجود
        ('out_of_stock', 'Out of Stock'),  # ناموجود
        ('pending', 'Pending'),  # در حال بررسی
        ('shipped', 'Shipped'),  # در حال ارسال
    ]

    brand = models.CharField(max_length=200)
    title = models.CharField(max_length=120, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(unique=True)
    quantity = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=PUBLISH_STATUS_CHOICES, default='draft')
    situation = models.CharField(max_length=30, choices=PRODUCT_STATUS_CHOICES, default='pending')
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product_image = models.ImageField(upload_to='product_images/')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    

class Order(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
]
    
    customer = models.ForeignKey(to=UserAccount, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    shipping_address = models.TextField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.BooleanField(default=False)
    shipped_at = models.DateTimeField(null=True, blank=True)
    delivered_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Order {self.id} by {self.customer.fullname}"
    

    @property
    def total_price_before_discount(self):
        return sum(item.total_price_before_discount for item in self.items.all())
    
    @property
    def total_price_with_discount(self):
        total = self.total_price_before_discount
        if total > Decimal("10000000"):
            return total * Decimal("0.9")
        return total


    
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


    
    


    