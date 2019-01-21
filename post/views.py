from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import PostModelForm
from datetime import datetime


# Create your views here.

def index(request):
    context = {}
    posts = Post.objects.all()

    context['posts'] = posts
    return render(request,'index.html', context)


def details(request, post_id):
    context = {}

    context['posts'] = Post.objects.get(id=question_id)

    return render(request, 'detail.html', context)


def createpost(request):
    context ={}

    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
        else:
            context['form'] = form
            return render(request, 'createpost.html', context)
    else:
         context['form'] = PostModelForm(initial={'date_created': datetime.now().date()})
         return render(request, 'createpost.html', context)
