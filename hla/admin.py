from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . models import Data
from . models import Req

# Register your models here.

admin.site.register(Data)
admin.site.register(Req)