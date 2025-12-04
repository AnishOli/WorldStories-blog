from django.shortcuts import get_object_or_404, redirect, render
from django.http import  HttpResponse
from blogs.models import Blog, Category
from django.db.models import Q

# Create your views here.
def posts_by_category(request, category_id):


    # print(category_id)

    posts = Blog.objects.filter(status ="Published", category = category_id)
    #try/except when we want to do custom action if the category doesnot exists

    # try:
    #     category = Category.objects.get(pk = category_id)
    # except:
    #     #redirect to the home page
    #     return redirect('home')
    
    #use this one when you want to show 404 error page
    category = get_object_or_404(Category,pk = category_id)

    context = {
        'posts':posts,
        'category_id':category,
    }
    return render(request, 'posts_by_category.html', context)




def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug= slug, status = "Published")
    #print(single_blog.featured_image.url)
    context = {
        'single_blog' :single_blog,
    }
    return render(request, 'blogs.html', context )


def search(request):
    keyword =  request.GET.get('keyword')
    blogs= Blog.objects.filter(Q(title__icontains = keyword)| Q(short_description__icontains = keyword)|Q(blog_body__icontains=keyword), status = "Published")
    #title__icontains = keyword this to search from title word

    context = {
        'keyword':keyword,
        'blogs':blogs,
    }
    return render (request, 'search.html', context)