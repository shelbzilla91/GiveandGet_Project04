from django.shortcuts import render
from .models import User, List

def User_index(request):
    context = {'users': User.objects.all()}
    return render(request, 'admin/User_index.html', context)


