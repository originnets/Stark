import os
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.shortcuts import render, get_object_or_404, reverse
from Arya import models
import json, datetime

@csrf_exempt
def Edit(request):
    """
    markdown文本编辑器
    """
    if request.method == "GET":
        '''
        获取数据库中的markdown文件
        '''
        md = models.Article.objects.filter(id=1).values('content_md')
        return render(request, 'edit.html', {"md": md[0]["content_md"]})
    if request.method == "POST":
        title = request.POST.get("title")
        desc = request.POST.get("desc")
        category = request.POST.get("category")
        tag = request.POST.get("tag")
        h5_txt = request.POST.get("html_txt")
        md_txt = request.POST.get("markdown_txt")
        is_recommend = request.POST.get("is_recommend")
        date_publish = datetime.datetime.now()
        get_tag = models.Tag.objects.get(name=tag)
        get_user = models.User(username="admin")
        get_category = models.Category.objects.get(name=category)
        new_data = models.Article(
            title=title,
            desc=desc,
            content_h5=h5_txt,
            content_md=md_txt,
            click_count=20,
            is_recommend=is_recommend,
            category=get_category,
            date_publish=date_publish,
            tag=get_tag,
        )
        new_data.save()
        new_data.user.add(get_user)
        new_data.save()
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

