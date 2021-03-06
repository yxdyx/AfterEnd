# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from ics_hdu_backend.service.chair_show_info import ChairInfoShow
from ics_hdu_backend.service.conference_show_info import ConferenceShow
from ics_hdu_backend.service.user_register_service import UserRegister
from ics_hdu_backend.service.conference_service import Conference
from ics_hdu_backend.service.chair_service import Chairsave


# Create your views here.
# html文件的url跳转
def index(request):
    """

    :param request:
    :return:
    """
    chair_brief_info = ChairInfoShow(number=-1, query_type='all').query_chair()
    conference_info = ConferenceShow().query_conference()
    index_list = {'chair': chair_brief_info, 'conference': conference_info}
    print(index_list)
    return render(request, 'index.html', {'index_list': index_list})


def chairs(request):
    """

    :param request:
    :return:
    """
    _chair_info = ChairInfoShow(number=-1, query_type='all').query_chair()
    return render(request, 'chairs.html', {'chair_list': _chair_info})


def conference(request):
    """

    :param request:
    :return:
    """
    conference_info = ConferenceShow().query_conference()
    return render(request, 'conference.html', {'conference_info': conference_info})


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


def register(request):
    """

    :param request:
    :return:
    """
    return render(request, 'register.html')


def figure(request, chair_id):
    """

    :param chair_id:
    :param request:
    :return:
    """
    chair = ChairInfoShow(number=chair_id, query_type='single').query_chair()[0]
    return render(request, 'figure.html', chair)


# 前端发送请求的接收

def user_register(request):
    """

    :param request:
    :return:
    """
    UserRegister(request)


def user_login(request):
    """

    :param request:
    :return:
    """
    pass


def add_chair(request):
    """
    必须返回json对象
    :param request:
    :return:
    """
    chair_save = Chairsave(request)
    chair_save.addOrupdatetime()
    chair_save.savechair()
    return HttpResponse('OK')


def add_conference(request):
    '''

    :param request
    :return:
    '''
    conference = Conference(request)
    conference.saveconference()
    return HttpResponse('OK')


def query_chair(request, query_type, number):
    """

    :param query_type:
    :param number:
    :param request:
    :return:
    """
    _chair_info = ChairInfoShow(number=number, query_type=query_type).query_chair().get_result_data()
    return HttpResponse(_chair_info)


def query_conference(request, session):
    pass
