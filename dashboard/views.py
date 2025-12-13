from django.shortcuts import render
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required

from accounts.views import user_login
from blogs.models import Blog, Category

# Create your views here.
@login_required (login_url= user_login)
def dashboard(request):
    category_count = Category.objects.all().count()
    #print(category_count)
    blog_count = Blog.objects.all().count()
    #print(blog_count)

    context = {
        'category_count':category_count  ,
        'blog_count': blog_count  ,
        'hide_categories': True
    }

    return render(request, 'dashboard/dashboard.html',context)



def categories(request):

    context ={
        'hide_categories':True,
    }
    return render (request, 'dashboard/categories.html', context)