from django.conf import settings
from ics_hdu_backend.models import Chair
from ics_hdu_backend.models import Manage_Chair_Conference
from ics_hdu_backend.utils.ret_obj import ResultData
import datetime


class ChairInfoShow(object):
    def __init__(self, chair_id, session=datetime.datetime.now().year, query_type='single'):
        """

        :param chair_id:
        :param session:
        :param query_type: 查询方式 {单查询：single, 全部查询：all, 按会议年份查询：session]
        """
        self.tmp = None
        self.chair_id = chair_id
        self.session = session
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
        return self.json_utils.query_data_beautify(result_data=self.tmp).get_result_data()

    def __get_chair_info_by_chair_id(self):
        """
        按chair_id查询
        :return:
        """
        self.tmp = Chair.objects.filter(chair_id=self.chair_id)

    def __get_chair_info_by_session(self):
        """
        按session查询
        :return:
        """
        self.tmp = Manage_Chair_Conference.objects\
                                          .filter(session=self.session)\
                                          .select_related('Chair')

    def __get_chair_info_all(self):
        """
        查询全部信息
        :return:
        """
        self.tmp = Chair.objects.all()

