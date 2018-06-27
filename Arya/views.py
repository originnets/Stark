import os
from django.shortcuts import render, get_object_or_404, reverse
from Stark import settings
from Arya import models


def Edit(request):
    """
    文本编辑器
    """
    if request.method == "POST":
        Abody = request.POST.get("Abody")
        Title = request.POST.get("title",None)
        Category = request.POST.get("category")
        if Title:
            models.Article.objects.create(ar_name=Title, category=Category)
            v = models.Article.objects.filter().first()
            print(v)
            w_url = os.getcwd()  # 获取当前工作目录
            os.chdir(os.path.abspath('static\md'))  # 改变当前工作目录
            with open(Title + ".md", 'w+') as f:  # 文件写入
                 f.write(Abody)
            os.chdir(w_url)  # 还原当前工作目录
            return render(request, 'edit.html')
        else:
            return render(request, 'edit.html')