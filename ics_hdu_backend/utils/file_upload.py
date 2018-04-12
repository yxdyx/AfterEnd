from django.conf import settings
import base64


class Multimedia(object):
    def __init__(self, instance, filename):
        """

        :param instance:
        :param filename: 文件名
        """
        self._instance = instance
        self._filename = filename
        self.upload_to()

    def upload_to(self):
        """
        接收源文件二进制编码数据，将二进制编码数据进行保存
        :return:
        """
        splitName = self._filename.split('.')
        nameBase = base64.b64encode(splitName[0].encode('utf-8'))
        realName = str(nameBase, 'utf-8') + '.' + splitName[len(splitName) - 1]
        return '/'.join([settings.STATIC_ROOT,
                         'images',
                         'chair',
                         self._instance.chair_id + self._instance.img_year + realName])

def upload_to(instance, filename):
    splitname = filename.split('.')
    namebase = base64.b64encode(splitname[0].encode('utf-8'))
    realname = str(namebase, 'utf-8') + '.' + splitname[len(splitname) - 1]
    return '/'.join([settings.STATIC_ROOT, 'images', 'chair', instance.chair_id, instance.session, realname])
