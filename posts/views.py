from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render

#from blog.posts.forms import CommentForm

from django.contrib.auth.models import User, Group
from .models import Post, Comment
from .forms import CommentForm

from django.utils import timezone

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer,PostSerializer

from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


def index(request):
    latest_posts_list = Post.objects.order_by('-post_date')[:5]
    template = loader.get_template('posts/index.html')
    context = {
        'latest_posts_list':  latest_posts_list,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'posts/base.html', {'latest_posts_list':  latest_posts_list,})

# Leave the rest of the views (detail, results, vote) unchanged


def detail(request, post_id):
    viewpost = get_object_or_404(Post, pk=post_id)
    comments_list = Comment.objects.filter(post = viewpost)
    #return HttpResponse(post.post_title)
    return render(request, 'posts/post.html', {'post': viewpost, 'comments_list': comments_list})

def results(request, post_id):
    response = "You're looking at the results of post %s."
    return HttpResponse(response % post_id)

def comment(request, post_id):
    if request.method == 'POST':
        print(request.POST.get('comment_author',''))
        comment = Comment()
        post = get_object_or_404(Post, pk=post_id)
        comment.comment_author = request.POST.get('comment_author','')
        comment.comment_text = request.POST.get('comment_text','')
        comment.post = post
        comment.comment_date = timezone.now()
        comment.save()
        post = get_object_or_404(Post, pk=post_id)
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("posts:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="posts/register.html", context={"register_form":form})