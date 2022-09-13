from django.contrib import admin
from .models import fpuserdata
from .models import RegisteredUser
# Register your models here.
admin.site.register(fpuserdata)
admin.site.register(RegisteredUser)
