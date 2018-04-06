class UserLogin(object):
    def __init__(self, request):
        self.__user_name = request.POST['username']
        self.__user_pwd = self.request.POST['password']

    def get_user_from_db(self):
        """
        根据用户名从数据库中取出对象，进行登陆相关操作
        :return:
        """
        pass

    def __info_compare(self):
        """
        登陆信息与数据库中信息进行比对
        :return:
        """
        pass

    def __info_verify(self):
        """
        登陆信息的安全验证->{正则表达式进行验证} 
        :return:
        """
        pass

