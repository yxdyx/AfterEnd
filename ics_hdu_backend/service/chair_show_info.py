from ics_hdu_backend.models import Chair
from ics_hdu_backend.utils.ret_obj import ResultData
from ics_hdu_backend.model import DB as sql


class ChairInfoShow(object):
    def __init__(self, number, query_type='single'):
        """

        :type number: object
        :param query_type: 查询方式 {单查询：single, 全部查询：all, 按会议年份查询：session]
        """
        self.tmp = None
        self.number = number
        self.query_type = query_type
        self.json_utils = ResultData()

    def query_chair(self):
        """
        查询借口
        :return:
        """
        if self.query_type == 'single':
            self.__get_chair_info_by_chair_id()
        elif self.query_type == 'all':
            self.__get_chair_info_all()
        else:
            self.__get_chair_info_by_session()
        return self.json_utils.query_data_beautify(result_data=self.tmp)

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
        self.tmp = Chair.objects.all()

