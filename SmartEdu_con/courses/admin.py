from django.contrib import admin
from . models import Course

# Register your models here.
# Course modelini admin alanında görmek için kayıt işlemi
admin.site.register(Course)