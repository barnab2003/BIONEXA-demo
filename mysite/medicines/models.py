from django.db import models

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='medicine_images/', blank=True, null=True)
    prescription_required = models.BooleanField(default=False)

    def __str__(self):
        return self.name
