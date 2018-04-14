from django.conf import settings
import base64


class Multimedia(object):
    def __init__(self):
        """

        """
        pass

    def upload_to(self, filename):
        """1
        接收源文件二进制编码数据，将二进制编码数据进行保存
        :type filename: object
        :return:
        """
        splitName = filename.split('.')
        nameBase = base64.b64encode(splitName[0].encode('utf-8'))
        realName = str(nameBase, 'utf-8') + '.' + splitName[len(splitName) - 1]
        return '/'.join([settings.STATIC_ROOT,
                         'images',
                         'chair',
                         str(self.chair_id), str(self.session), realName])
