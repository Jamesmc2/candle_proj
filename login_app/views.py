from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
import bcrypt
from time import gmtime, strftime
from datetime import datetime



def index(request):
    context = {
        'accounts' : User.objects.all(),
        }
    return render(request,'login_register.html',context)

def register(request):
    errors = User.objects.basic_validator_reg(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    new_user=User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = pw_hash, birthday = request.POST['birthday'])
    request.session['user_id'] = new_user.id
    request.session['user_name'] = new_user.first_name
    return redirect('/books')

def login(request):
    errors = User.objects.basic_validator_login(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    user = User.objects.filter(email = request.POST['email'])
    if user:
        if bcrypt.checkpw(request.POST['password'].encode(), user[0].password.encode()):
            request.session['user_id'] = user[0].id
            request.session['user_name'] = user[0].first_name
            return redirect('/books')
    return redirect('/')

def success(request):
    if not 'user_id' in request.session:
        return redirect('/')
    return render(request,'success.html')

def logout(request):
    del request.session['user_id']
    del request.session['user_name']

    return redirect('/')

def delete(request):
    User.objects.get(id=request.session['user_id']).delete()
    del request.session['user_id']
    del request.session['user_name']
    return redirect('/')