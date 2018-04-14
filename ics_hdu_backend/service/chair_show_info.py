from ics_hdu_backend.models import Chair
from ics_hdu_backend.utils.ret_obj import ResultData
from ics_hdu_backend.model import DB as sql


class ChairInfoShow(object):
    def __init__(self, number=-1, query_type='single'):
        """

        :type number: object {session or chair_id or -1}
        :param query_type: 查询方式 {单查询：single, 全部查询：all, 按会议年份查询：session]
        """
        self.tmp = None
        self.chair_list = []
        self.number = number
        self.query_type = query_type
        self.json_utils = ResultData()

    def query_chair(self):
        """
        查询借口
        :return:
        """
        if self.query_type == 'single' and self.number != -1:
            self.__get_chair_info_by_chair_id()
        elif self.query_type == 'all' and self.number == -1:
            self.__get_chair_info_all()
        else:
            self.__get_chair_info_by_session()
        return self.query_data_beautify(result_data=self.tmp)

    def __get_chair_info_by_chair_id(self):
        """
        按chair_id查询
        :return:
        """
        self.tmp = Chair.objects.raw(sql.CHAIR_INFO_BY_CHAIR_ID, [self.number])

    def __get_chair_info_by_session(self):
        """
        按session查询
        :return:
        """
        self.tmp = Chair.objects.raw(sql.CHAIR_INFO_BY_SESSION, [self.number])

    def __get_chair_info_all(self):
        """
        查询全部信息
        :return:
        """
        self.tmp = Chair.objects.raw(sql.CHAIR_INFO_BY_ALL)

    def query_data_beautify(self, result_data):
        """
        查询结果数据格字典式化
        :return:
        """
        for _data in result_data:
            self.chair_list.append({'chair_id': _data.chair_id,
                                    'chair_name': _data.chair_name,
                                    'chair_org': _data.chair_org,
                                    'chair_pic_url': _data.chair_pic_url,
                                    'chair_info': _data.chair_info})
        return self.chair_list
