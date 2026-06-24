from django.db import models
from django.contrib.auth.models import User
from medicines.models import Medicine

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.medicine.name} (x{self.quantity})"

    def total_price(self):
        return self.medicine.price * self.quantity
