from django.shortcuts import render
from django import forms
from django.http import HttpResponse

import os,base64
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

class UserForm(forms.Form):
    year = forms.CharField()
    month = forms.CharField()
    headImg = forms.FileField()

def upload(request):
    if request.method == "POST":
        inf = UserForm(request.POST,request.FILES)
        if inf.is_valid():
            #获取表单信息
            year = inf.cleaned_data['year']
            month = inf.cleaned_data['month']
            headImg = inf.cleaned_data['headImg']
            backname=str(headImg).split('.')
            image=["jpg","bmp","png","jpeg"]
            mov=["mp4","3gp","mpg","avi","wmv","flv","swf"]
            #路径需要修改
            pathdir='/Users/feiyu/Codes/WebDesigh/test1/'
            if backname[1].lower() in image:
                ba = base64.b64encode('headImg.name'.encode('utf-8'))
                path=default_storage.save(pathdir+'/media/image/'+str(year)+'/'+str(month)\
                +'/'+str(ba,'utf-8')+str('.')+str(backname[1]),ContentFile(headImg.read()))
                tmp_file=os.path.join(settings.MEDIA_ROOT,path)
            elif backname[1].lower() in mov:
                ba = base64.b64encode('headImg.name'.encode('utf-8'))
                path=default_storage.save(pathdir+'/media/movie/'+str(year)+'/'+str(month)\
                +'/'+str(ba,'utf-8')+str('.')+str(backname[1]),ContentFile(headImg.read()))
                tmp_file=os.path.join(settings.MEDIA_ROOT,path)
            return HttpResponse('upload ok!')
    else:
        inf = UserForm()
    return render(request,'upload.html',{'inf':inf})
