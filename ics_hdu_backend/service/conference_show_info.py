from datetime import datetime
from ics_hdu_backend.models import Conference
from ics_hdu_backend.model import DB as sql
from ics_hdu_backend.utils.ret_obj import ResultData
from ics_hdu_backend.utils.time_format import TimeFormat


class ConferenceShow(object):
    """
    by: liaochuntao
    """
    def __init__(self, session=datetime.now().year):
        self.session = session
        self.tmp = None
        self.json_utils = ResultData()
        self.conference_list = []

    def query_conference(self):
        self.tmp = Conference.objects.raw(sql.CONFERENCE_CHAIR_INFO_BY_SESSION, [self.session])
        return self.__query_data_beautify(result_data=self.tmp)

    def __query_data_beautify(self, result_data: Conference):
        for _conference in result_data:
            self.conference_list.append({'conference_id': _conference.conference_id,
                                         'session': _conference.session,
                                         'conference_topic': _conference.conference_topic,
                                         'conference_start_time': TimeFormat(time=_conference.conference_start_time).time_str_analyze(),
                                         'conference_end_time': TimeFormat(time=_conference.conference_end_time).time_str_analyze(),
                                         'conference_locations': _conference.conference_locations})
        return self.conference_list
