from django.contrib import admin
from .models import Profile

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    # exclude = ('email', 'created_by', 'created_at', 'updated_by', 'updated_at') #----EXCLUDE FIELDS---------
    readonly_fields = ('created_at',)
    list_display = ('full_name', 'mobile', 'contactperson', 'capital_name') #--TABLE VIEW OF MODELS-----

    # fields = (('fname', 'lname'), 'mobile', 'contactperson', 'mobileofcontactperson') # ------TRIMMING OF FIELDS IN ADMIN---

    fieldsets = (
        ('Information', {
        'fields': ('fname', 'lname', 'mobile', 'email', 'contactperson', 'mobileofcontactperson')
    }), 
    ('Editors', {
        'classes': ('collapse',),
        'fields': ('created_by', 'created_at', 'updated_by', 'updated_at')
    })) #----FIELD DETAILS WITH HEADER AND COLLAPSEABLE FIELDS-----

    def full_name(self, obj):
        return f"{obj.fname} {obj.lname}" #---JOINING OF FIELDS---
    
    @admin.display(description='FULLNAME NEW')
    def capital_name(self, obj):
        return f"{obj.fname} {obj.lname}" #---JOINING OF FIELDS---

admin.site.register(Profile, ProfileAdmin)
