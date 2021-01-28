from django.contrib import admin

# Register your models here.
from .models import Movements, Account_value

admin.site.register(Movements)
admin.site.register(Account_value)
