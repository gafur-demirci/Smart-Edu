from django.contrib import admin
from . models import Course, Category, Tag

# Register your models here.
# Course modelini admin alanında görmek için kayıt işlemi
# admin.site.register(Course)
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'available')
    list_filter = ('available',)
    search_fields = ('name', 'description')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}