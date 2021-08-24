from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.views import View
from blogs.models import BlogModel, CategoryModel, CommentModel
from blogs.forms import CommentForm
from django.db.models import Q

# Create your views here.

class HomePageView(View):

    def get(self, request):
        blogs = BlogModel.objects.order_by('-id')
        result = -1
        search = self.request.GET.get('search')

        if search: 
            search = self.request.GET.get('search')
            blogs = blogs.filter(
                Q(title__icontains=search) |
                Q(context__icontains=search)
            )
            result = len(blogs)

        context = {
            'blogs' : blogs,
            'search' : search,
            'result' : result,
        }

        return render(request, 'pages/homepage.html', context)


class CategoryPageView(View):

    def get(self, request, name):
        category = get_object_or_404(CategoryModel, name=self.kwargs['name'])
        blogs = category.blogs.order_by('-id')

        context = {
            'category' : category,
            'blogs' : blogs,
        }

        return render(request, 'pages/categorypage.html', context)


class BlogDetailView(View):
    form = CommentForm()

    def get(self, request, slug):
        blog = get_object_or_404(BlogModel, slug=slug)
        comments = blog.comments.order_by('-id').filter(parent=None)
        blog.views_time += 1
        blog.save()
        form = CommentForm()
        context = {
            'blog' : blog,
            'comments' : comments,
            'form' : form,
        }
        return render(request, 'pages/detail.html', context)

    def post(self, request, slug):
        blog = get_object_or_404(BlogModel, slug=slug)
        comments = blog.comments.order_by('-id').filter(parent=None)
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            if request.POST.get('answer') != 'A':
                comment.parent = get_object_or_404(CommentModel, id=request.POST.get('answer'))
            comment.save()
            blog.comment_number += 1
            blog.save()
            return redirect('blogs:detailpage', slug=blog.slug)



    
