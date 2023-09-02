from django.contrib import admin

# Register your models here.

from .models import UserProfile
from .models import BusinessProfile
from .models import Category
from .models import Review

admin.site.register(UserProfile)
admin.site.register(BusinessProfile)
admin.site.register(Category)
admin.site.register(Review)