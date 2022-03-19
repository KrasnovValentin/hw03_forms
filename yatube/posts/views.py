from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest
from .models import Post, Group, User
from posts.forms import PostForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import datetime


def index(request: HttpRequest) -> HttpResponse:
    """Модуль отвечающий за главную страницу"""
    posts: str = Post.objects.all()
    paginator = Paginator(posts, 10)
    page_number: int = request.GET.get('page')
    page_obj: int = paginator.get_page(page_number)
    context: dict = {
        'posts': posts,
        'page_obj': page_obj,
        'title': 'Последние обновления на сайте',
    }
    return render(request, 'posts/index.html', context)


@login_required
def group_posts(request: HttpRequest, slug: str) -> HttpResponse:
    """Модуль отвечающий за страницу сообщества"""
    group = get_object_or_404(Group, slug=slug)
    posts: str = Post.objects.filter(group=group)
    paginator = Paginator(posts, 10)
    page_number: int = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context: dict = {
        'group': group,
        'posts': posts,
        'page_obj': page_obj,
        'title': f'Записи сообщества {slug}',
    }
    return render(request, 'posts/group_list.html', context)


@login_required
def profile(request: HttpRequest, username) -> HttpResponse:
    """Модуль отвечающий за личную страницу"""
    author = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=author)
    posts_count = author.posts.count()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts_count': posts_count,
        'author': author,
        'page_obj': page_obj,
    }
    return render(request, 'posts/profile.html', context)


@login_required
def post_detail(request: HttpRequest, post_id: int) -> HttpResponse:
    """Модуль отвечающий за просмотр отдельного поста"""

    post = get_object_or_404(
        Post.objects
            .select_related('author')
            .select_related('group'), id=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})


@login_required
def post_create(request: HttpRequest) -> HttpResponse:
    """Модуль отвечающий за страницу создания текста постов."""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.pub_date = datetime.datetime.now()
            post.save()
            return redirect('posts:profile', request.user)
        return render(request, 'posts/create_post.html', {'form': form, })
    form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form, })


@login_required
def post_edit(request: HttpRequest, post_id: int) -> HttpResponse:
    """Модуль отвечающий за страницу редактирования текста постов."""
    post: str = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post.text = form.cleaned_data['text']
            post.group = form.cleaned_data['group']
            post.author = request.user
            post.save()
            return redirect('posts:profile', request.user)
        else:
            context = {
                'form': form,
                'is_edit': True,
            }
        return render(request, 'posts/create_post.html', context)
    else:
        if request.user == post.author:
            form = PostForm(instance=post)
            context = {
                'form': form,
                'is_edit': True,
            }
            return render(request, 'posts/create_post.html', context)
        else:
            return redirect('posts:post_detail', post_id)
