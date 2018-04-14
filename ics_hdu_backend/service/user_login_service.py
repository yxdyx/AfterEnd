from django.http import HttpResponse
from ics_hdu_backend.models import  User
import base64
import hashlib

class UserLogin(object):
    def __init__(self, request):
        self.__user_name = request.POST['username']
        self.__user_pwd = self.request.POST['password']

    def get_user_from_db(self):
        """
        根据用户名从数据库中取出对象，进行登陆相关操作
        :return:
        """
        user = User()
        username = base64.b64encode(self.__user_name.encode('utf8'))
        if user.object.filter(user_name = username):
            get_user = user.object.filter(user_name = self.__user_name)
            return get_user
        else:
            return HttpResponse('不存在用户')
        

    def __info_compare(self):
        """
        登陆信息与数据库中信息进行比对
        :return:
        """
        md5_pwd = self.get_user.user_pwd
        pwd = hashlib.md5(md5_pwd.encode('utf8')).hexdigest()

        if md5_pwd == pwd:
            return HttpResponse('ok')
        else:
            return HttpResponse('密码错误')
    def __info_verify(self):
        """
        登陆信息的安全验证->{正则表达式进行验证} 
        :return:
        """
        pass