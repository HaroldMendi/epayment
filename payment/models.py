from django.db import models
from profiles.models import Profile
from house.models import House

# Create your models here.

class Payment(models.Model):
    payee = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='payee', null=True, blank=False)
    block_number = models.ForeignKey(House, on_delete=models.DO_NOTHING, null=True, blank=False)
    amount_paid = models.IntegerField(blank=True, null=True)
    amount_to_pay = models.IntegerField(blank=True, null=True)
    payment_for_the_month_of = models.DateField(blank=True, null=True)
    balance = models.IntegerField(blank=True, null=True)
    date_paid = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.date_paid

