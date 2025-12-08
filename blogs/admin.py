from django.contrib import admin

from .models import Category,Blog


#to make auto generate slug
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

    list_display= ('title','category','author','status','is_featured')
    search_fields = ('id', 'title','category__category_name','status')
    list_editable = ('is_featured',)


# class CategoryAdmin(admin.ModelAdmin):
#     def has_add_permission(self, request):
#         totalCategory = Category.objects.all().count()
#         if totalCategory <=10:
#             return True
#         else:
#             return False
           
# Register your models here.
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
