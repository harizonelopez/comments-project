from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm, PostForm
from .models import Post

def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'home.html', context)

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = PostForm()

    context = {
        'form': form,
    }
    return render(request, 'create_post.html', context)

def post_detailview(request, id):
    post = get_object_or_404(Post, id=id)
    
    if request.method == 'POST':
        cf = CommentForm(request.POST)
        if cf.is_valid():
            comment = cf.save(commit=False)
            comment.post = post
            comment.save()
            cf = CommentForm()
    else:
        cf = CommentForm()
    
    context = {
        'post': post,
        'comment_form': cf,
    }
    
    return render(request, 'post_detail.html', context)

def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    
    return redirect('home')
