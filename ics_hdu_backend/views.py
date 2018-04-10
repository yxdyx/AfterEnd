# -*- coding: utf-8 -*-


from django.shortcuts import render


# Create your views here.
# html文件的url跳转
def index(request):
    """

    :param request:
    :return:
    """
    return render(request, 'index.html')


def chairs(request):
    """

    :param request:
    :return:
    """
    return render(request, 'chairs.html')


def conference(request):
    """

    :param request:
    :return:
    """
    return render(request, 'conference.html')


def about(request):
    """

    :param request:
    :return:
    """
    return render(request, 'about.html')


def team(request):
    """

    :param request:
    :return:
    """
    return render(request, 'team.html')


def figure(request, chair_id):
    """

    :param chair_id:
    :param request:
    :return:
    """
    print(chair_id)
    return render(request, 'figure.html')


# 前端发送请求的接收

def register(request):
    """

    :param request:
    :return:
    """
    pass


def login(request):
    """

    :param request:
    :return:
    """
    pass


def add_chair(request):
    """

    :param request:
    :return:
    """
    pass


def query_chair(request, chair_id):
    """

    :param request:
    :return:
    """
    pass


def query_conference(request, session):
    pass
