from django.conf import settings
import base64


class Multimedia(object):
    """
    更改图片上传路径
    by: junyachen
    """

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
        splitName = str(filename).split('.')
        nameBase = base64.b64encode(splitName[0].encode('utf-8'))
        realName = str(nameBase, 'utf-8') + '.' + splitName[len(splitName) - 1]
        return '/'.join(['static',
                         'images',
                         'human',
                         str(self.chair.chair_id), str(self.session), str(realName)])

    def picture_split(self, width=300, height=300):
        """
        利用opencv对图片进行裁剪（人脸的识别处理+图片大小的裁剪）
        :param width:
        :param height:
        :return:
        """
        pass

