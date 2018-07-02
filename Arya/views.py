import os
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.shortcuts import render, get_object_or_404, reverse
from Arya import models
import json

@csrf_exempt
def Edit(request):
    """
    markdown文本编辑器
    """
    if request.method == "GET":
        md = models.Article.objects.all().values('content_md')
        return render(request, 'edit.html', {"md": md[0]["content_md"]})
    if request.method == "POST":
        title = request.POST.get("title")
        desc = request.POST.get("desc")
        category = request.POST.get("category")
        tag = request.POST.get("tag")
        h5_txt = request.POST.get("html_txt")
        md_txt = request.POST.get("markdown_txt")
        is_recommend = request.POST.get("is_recommend")
        print(h5_txt)
        #models.Article.objects.create(title=title, desc=desc, category_id=category, tag_id=tag, content_h5=h5_txt, content_md=md_txt, is_recommend=is_recommend)
        return render(request, 'edit.html',)


def Admin(request):
    return render(request, 'admin.html')

def Index(request):
    return render(request, 'index.html')

def page_not_found(request):
    return render(request, '404.html')

def About(request):
    return render(request, 'about.html')

def Comment(request):
    return render(request, 'comment.html')

def Message(request):
    return render(request, 'message.html')

def Details(request):
    return render(request, 'details.html')

