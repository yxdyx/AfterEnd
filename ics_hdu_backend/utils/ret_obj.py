import json


class ResultData(object):
    """
    返回数据json格式化
    by: liaochuntao
    """

    def __init__(self):
        """
        将传入的数据对象json字符串格式化
        """
        pass

    @staticmethod
    def get_result_data(data):
        """
        获取经过json格式化后的数据
        :param data:
        :return:
        """
        return json.dumps(obj=data)
