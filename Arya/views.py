import os
from django.shortcuts import render, get_object_or_404, reverse


from Stark import settings


def Edit(request):
    """
    文本编辑器
    """
    if request.method == "POST":
        Abody = request.POST.get("Abody")
        Title = request.POST.get("title")

        w_url = os.getcwd()  # 获取当前工作目录
        os.chdir(os.path.abspath('static\md'))  # 改变当前工作目录
        with open(Title + ".md", 'w+') as f:  # 文件写入
             f.write(Abody)
        os.chdir(w_url)  # 还原当前工作目录

    return render(request, 'edit.html')