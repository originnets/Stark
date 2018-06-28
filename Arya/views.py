import os
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.shortcuts import render, get_object_or_404, reverse
from Arya import models
from Stark import settings

@csrf_exempt
def Edit(request):
    """
    markdown文本编辑器
    """
    if request.method == "GET":
        v = models.Article.objects.filter().all()
        print(v[0])
        return render(request, 'edit.html', {"v": v})
    if request.method == "POST":
        Abody = request.POST.get("Abody")
        Title = request.POST.get("title", None)
        Category = request.POST.get("category", None)
        v = models.Article.objects.all()
        if Title and Category:
            models.Article.objects.create(ar_name=Title, category=Category)
            w_url = os.getcwd()  # 获取当前工作目录
            os.chdir(os.path.abspath('static\md'))  # 改变当前工作目录
            with open(Title + ".md", 'w+') as f:  # 文件写入
                f.write(Abody)
            os.chdir(w_url)  # 还原当前工作目录
            return render(request, 'edit.html', )
        else:
            return render(request, 'edit.html', )

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

