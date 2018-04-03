"""ICSHDU URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ics_hdu_backend import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # html文件url地址
    # 首页
    path(r'^index/', views.index),
    # 会议
    path(r'^conference/', views.conference),
    # 主席
    path(r'^chair/', views.chairs),
    # 关于
    path(r'^about/', views.about),

    # 前端请求的url
    # 用户注册
    path(r'^user_register/', views.register),
    # 用户登陆
    path(r'^user_login/', views.login),
    # 主席信息录入
    path(r'^add_chair/', views.add_chair),
    # 查询主席信息
    path(r'^chair/<int: chair_id>', views.query_chair),
    # 根据session查询所有会议信息
    path(r'^/conference/<int: session>/query_all_conference', views.query_conference),


]
