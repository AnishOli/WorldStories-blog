from django.shortcuts import render

from blogs.models import Category,Blog


def home(request):
    #categories = Category.objects.all() #not needed because we already pass in context processors.py 
    featured_posts = Blog.objects.filter(is_featured= True, status = "Published").order_by('-updated_at')
    posts = Blog.objects.filter(is_featured= False , status = "Published")

    context = {
        #'categories': categories,
        'featured_posts':featured_posts,
        'posts':posts
    }
    return render(request, 'home.html',context)


