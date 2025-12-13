from django.shortcuts import render
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required

from accounts.views import user_login

# Create your views here.
@login_required (login_url= user_login)
def dashboard(request):
    return render(request, 'dashboard/dashboard.html',{'hide_categories': True})