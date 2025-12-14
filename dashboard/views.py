from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required

from accounts.views import user_login
from blogs.models import Blog, Category
from dashboard.forms import CategoryForm

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