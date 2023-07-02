from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to='DP/', blank=True)
    customer_pop_message = models.TextField(max_length=120, blank=True)

    def __str__(self):
        return self.user.username


class Transactions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    debit = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    credit = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction for {self.user.username}"

    def save(self, *args, **kwargs):
        self.balance = self.balance + self.credit - self.debit
        super().save(*args, **kwargs)
