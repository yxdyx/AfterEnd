from django.http import HttpResponse
from ics_hdu_backend.models import User
import hashlib 
import base64

class UserRegister(object):
    def __init__(self, request):
        self.register_code = request.POST['register_code']
        self.user_name = request.POST['username']
        self.user_pwd = request.POST['password']
        self.user_email = request.POST['email']

    def __info_verify(self):
        """
        注册信息验证
        :return:
        """
        pass

    def __user_exist(self):
        """
        判断user_email、user_name是否存在
        :return:
        """
        user = User()
        if user.object.filter(user_name = self.user_name):
            return HttpResponse('用户名存在')
        elif user.object.filter(user_email = self.user_email):
            return HttpResponse('邮箱存在')
        else:
            return HttpResponse('注册成功')

    def __save_user(self):
        """
        :return:HttpResponser
        """
        #使用base64加密
        base64_user_name = base64.b64encode(self.user_name.encode('utf8'))
        #使用md5加密
        md5_password = hashlib.md5(self.user_pwd.encode('utf8')).hexdigest()

        user = User()
        user.user_name = base64_user_name
        user.user_pwd = md5_password
        user.user_email = self.user_email
        user.save()
        return HttpResponse('注册成功')