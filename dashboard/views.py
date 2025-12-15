from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required

from accounts.views import user_login
from blogs.models import Blog, Category
from dashboard.forms import BlogPostForm, CategoryForm
from django.template.defaultfilters import slugify



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


def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            # try:
                form.save()
                messages.success(request, "Category added successfully!")
                return redirect('categories')
        #     except IntegrityError:
        #         # Catches the unique constraint violation
        #         messages.error(request, "Sorry, this category already exists")
        # else:
        #     messages.error(request, "Invalid data. Please check the fields.")
    else:
        form = CategoryForm()

    context = {
        'form': form,
        'hide_categories': True,
    }
    return render(request, "dashboard/add_category.html", context)


def edit_category(request, pk):
     category = get_object_or_404(Category, pk=pk)
     if request.method == "POST":
          form = CategoryForm(request.POST, instance=category)
          if form.is_valid():
               form.save()
               return redirect("categories")
     form = CategoryForm( instance=category)    


    

     context = {
          
        'form':form,
        'hide_categories': True,
        'category':category,
    }
     return render(request, "dashboard/edit_category.html",context)
     

def delete_category(request, pk):
     category = get_object_or_404(Category, pk=pk)
     category.delete()
     return redirect('categories')




# for blog

def blog_posts(request):
     posts= Blog.objects.all()
     context= {
          'posts':posts,
          'hide_categories':True
     }
     return render(request, 'dashboard/blog_posts.html',context)

# from django.utils.text import slugify


# def generate_unique_slug(title):
#     base_slug = slugify(title)
#     slug = base_slug
#     counter = 1
#     while Blog.objects.filter(slug=slug).exists():
#         slug = f"{base_slug}-{counter}"
#         counter += 1
#     return slug


def add_posts(request):
     if request.method == "POST":
        form = BlogPostForm(request.POST,request.FILES)
        # if form.is_valid():
        #     post = form.save(commit=False)
        #     post.author = request.user
        #     post.slug = generate_unique_slug(form.cleaned_data['title'])
        #     post.save()
        #     messages.success(request, "Blogs added successfully!")
        #     return redirect('blog_posts')
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user 
            post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-' +str(post.id)
            post.save()
            messages.success(request, "Blogs added successfully!")
            return redirect('blog_posts')
        # else:
        #      print("Error")
        #      print(form.errors)
     else:
        form = BlogPostForm()
     context= {
          'form': form,
          'hide_categories': True,
     }
     return render(request, "dashboard/add_posts.html", context)
    

def edit_posts(request,pk):
     post = get_object_or_404(Blog,pk=pk)
     if request.method == "POST":
          form = BlogPostForm(request.POST, instance=post)
          if form.is_valid():
               form.save()
               return redirect('blog_posts')
     else:
        form = BlogPostForm(instance=post)
     
     context ={
          'form':form,
          'hide_categories':True,
          'post':post,
     }

     return render(request, 'dashboard/edit_posts.html',context )


def delete_posts(request, pk):
     post = get_object_or_404(Blog, pk=pk)
     post.delete() 
     return redirect('blog_posts')