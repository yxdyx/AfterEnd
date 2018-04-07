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
        pass

    def __save_user(self):
        """

        :return:
        """
        pass
