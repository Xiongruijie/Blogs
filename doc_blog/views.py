from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from .models import *
import markdown
import re
# Create your views here.

def default_index(request):
    return render(request, 'doc_blog/index.html', context={'title': '博客世界', 'welcome': '欢迎欢迎'})

def index(request):
    post_list = Post.objects.all().order_by('-create_time')
    return render(request, 'doc_blog/index.html', context={'post_list': post_list})

def archive(request, year, month):
    post_list = Post.objects.filter(
        create_time__year=year,
        create_time__month=month
    ).order_by('-create_time')
    return render(request, 'doc_blog/index.html', context={'post_list': post_list})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        TocExtension(slugify=slugify),
    ])
    post.body = md.convert(post.body)
    # post.toc = md.toc

    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''

    return render(request, 'doc_blog/detail.html', context={'post': post})

def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-create_time')
    return render(request, 'doc_blog/index.html', context={'post_list': post_list})

def tag(request, pk):
    t = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=t).order_by('-create_time')
    return render(request, 'doc_blog/index.html', {'post_list': post_list})








