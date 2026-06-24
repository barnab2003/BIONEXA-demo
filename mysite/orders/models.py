from django.db import models
from django.contrib.auth.models import User
from medicines.models import Medicine

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

    @property
    def total_price(self):
        return sum(item.medicine.price * item.quantity for item in self.items.all())
    STATUS_CHOICES = [
        ('Placed', 'Placed'),
        ('Cancelled', 'Cancelled'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Placed')
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.medicine.name} (x{self.quantity})"
