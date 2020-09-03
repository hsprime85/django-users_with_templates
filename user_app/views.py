from django.shortcuts import render, redirect
from .models import Users


def index(request):
    context = {
        'user_info': Users.objects.all()
    }
    print(context['user_info'])
    return render(request, 'index.html', context)


def add_user(request):
    print(request.POST)

    # add item to DB
    Users.objects.create(
        user_id=request.POST['user_id'],
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        age=request.POST['age'],
    )

    return redirect('/')
