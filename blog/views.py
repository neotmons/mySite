#from django.contrib.auth.mixins import LoginRequiredMixin
#from django.http import JsonResponse
#from django.views.generic import CreateView, UpdateView

from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html')

def post_new(request):
    return render(request, 'blog/post_new.html')

def post_detail(request):
    return render(request, 'blog/post_detail.html')

def post_edit(request):
    return render(request, 'blog/post_edit.html')

def post_delete(request):
    return render(request, 'blog/post_delete.html')

def comment_list(request):
    return render(request, 'blog/comment_list.html')

def comment_edit(request):
    return render(request, 'blog/comment_edit.html')

def comment_delete(request):
    return render(request, 'blog/comment_delete.html')