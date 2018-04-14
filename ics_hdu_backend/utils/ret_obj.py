import json


class ResultData(object):
    """
    返回数据json格式化
    """

    def __init__(self):
        """
        将传入的数据对象json字符串格式化
        """
        self.tmp = []

    def query_data_beautify(self, result_data):
        """

        :return:
        """
        for _data in result_data:
            self.tmp.append({'chair_id': _data.chair_id,
                             'chair_name': _data.chair_name,
                             'chair_org': _data.chair_org,
                             'chair_pic_url': _data.chair_pic_url,
                             'chair_info': _data.chair_info})
        return self

    def get_result_data(self):
        """
        获取经过json格式化后的数据
        :return: str
        """
        return json.dumps(obj=self.tmp)
