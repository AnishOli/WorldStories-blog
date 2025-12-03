
# this is done to get access of category in all page without doing context dict in every function
from django.urls import resolve
from blogs.models import Category

def get_categories(request):
    view_name = resolve(request.path_info).url_name
    if view_name in ['home', 'posts_by_category']:  # only for these views we will write here where we need it 
        categories = Category.objects.all()
        return {'categories': categories}
    return {}
