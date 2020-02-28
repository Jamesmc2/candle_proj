from django.shortcuts import render, redirect
from .models import Event, Blog, Comment
from login_app.models import User

# Create your views here.

def main(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def social(request):
    context = {
        'events' : Event.objects.all(),
        'blogs' : Blog.objects.all().order_by('-created_at'),
    }
    return render(request, 'social.html', context)

def comment(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    user = User.objects.get(id=request.session['user_id'])
    Comment.objects.create(user=user,blog=blog,text=request.POST['comment'])
    return redirect('/social')
