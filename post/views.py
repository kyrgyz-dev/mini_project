from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from post.models import Post
from post.forms import PostForm


def detail_post(request, pk):
    user = request.user
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post/detail.html', {'post': post, 'user': user})


@login_required
def create_post(request):
    user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = user
            post.save()
            messages.success(request, 'Пост успешно создан')
            return redirect('post:detail-post', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post/create.html', {'form': form, 'user': user})


@login_required
def edit_post(request, pk):
    user = request.user
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пост успешно обновлен')
            return redirect('post:detail-post', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post/edit.html', {'form': form, 'post': post, 'user': user})


@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('index')
