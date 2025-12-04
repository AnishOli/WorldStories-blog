
# this is done to get access of category in all page without doing context dict in every function
from django.urls import resolve
from assignments.models import SocialLink
from blogs.models import Category

def get_categories(request):
    view_name = resolve(request.path_info).url_name
    if view_name in ['home', 'posts_by_category','blogs','search',]:  # only for these views we will write here where we need it 
        categories = Category.objects.all()
        return {'categories': categories}
    return {}

def get_social_links(request):
    view_name = resolve(request.path_info).url_name
    if view_name in ['home', 'posts_by_category', 'blogs',]:
        social_links = SocialLink.objects.all()
        return{'social_links':social_links}
    return{}
    