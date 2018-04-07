from django import forms
from django.http import HttpResponse

import os, base64
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import render


class UserForm(forms.Form):
    chair_id = forms.CharField()
    year = forms.CharField()
    headImg = forms.FileField()


# 输入参数：chair_id、年、图片、切割后的图片名字
# 功能：保存图片
def is_image(chair_id, year, headImg, backname):
    ba = base64.b64encode(backname[0].encode('utf-8'))
    # 文件相对路径
    r_path = 'images/chair/' + str(chair_id) + '/' + str(year) + '/' + \
             str(ba, 'utf-8') + str('.') + str(backname[1])
    path = default_storage.save('stastic/' + r_path, ContentFile(headImg.read()))
    # 文件绝对路径
    a_path = os.path.join(settings.STATIC_ROOT, r_path)


# 输入参数：request对象
# 功能：获取chair_id、年属性并根据文件后缀名判断是否为图片或视频，并予以保存
# 返回参数：HttpResponse对象
def upload(request):
    if request.method == "POST":
        inf = UserForm(request.POST, request.FILES)
        if inf.is_valid():
            # 获取表单信息
            chair_id = inf.cleaned_data['chair_id']
            year = inf.cleaned_data['year']
            headImg = inf.cleaned_data['headImg']
            backname = str(headImg).split('.')
            image = ["jpg", "bmp", "png", "jpeg"]
            # 根据文件后缀名判断是否为图片
            if backname[1].lower() in image:
                is_image(chair_id, year, headImg, backname)
            return HttpResponse('upload ok!')
    else:
        inf = UserForm()
    return render(request, 'upload.html', {'inf': inf})
