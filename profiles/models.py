from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    fname = models.CharField(max_length=100, null=True, blank=False)
    lname = models.CharField(max_length=100, null=True, blank=False)
    email = models.CharField(max_length=100,blank=True, null=True)
    mobile = models.DecimalField(max_digits=11, decimal_places=0, null=True,blank=True)
    contactperson = models.CharField(max_length=100,blank=True, null=True)
    mobileofcontactperson = models.DecimalField(max_digits=11,decimal_places=0, blank=True, null=True)
    slug = AutoSlugField(populate_from='fname', unique_with=('id','lname'))
    created_at = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='updated_by')
    updated_at = models.DateTimeField(null=True, blank=True)


    # @property
    # def full_name(self):
    #     return f"{self.fname} {self.lname}"

    # def __str__(self):
    #     return self.full_name

    def __str__(self):
        return f"{self.fname} {self.lname}"

    # def __str__(self):
    #     return self.lname