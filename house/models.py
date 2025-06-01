from django.db import models
from profiles.models import Profile
from django.contrib.auth.models import User

# Create your models here.

class House(models.Model):
    block_number = models.IntegerField(null=False, blank=False, default=0)
    lot_number = models.IntegerField(null=False, blank=False, default=0)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='owner' ,null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, editable=False)

    def __int__(self):
        return self.block_number