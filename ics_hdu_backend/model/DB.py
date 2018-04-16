"""
by: liaochuntao

数据库查询sql语句

CHAIR_INFO_BY_CHAIR_ID: 通过chair_id查询指定的主席信息 （single）

CHAIR_INFO_BY_SESSION: 通过session查询指定的主席信息（s）

CONFERENCE_INFO_BY_SESSION: 通过session查询该届会议的所有分会议
"""

CHAIR_INFO_BY_ALL = 'select ' \
                        'c1.chair_id, c1.chair_name, c1.chair_org, c2.chair_pic_url ' \
                    'from ' \
                        'Chair c1 join ChairPic c2 ' \
                    'on ' \
                        'c1.chair_id=c2.chair_id'

CHAIR_INFO_BY_CHAIR_ID = 'select ' \
                            'c1.chair_id, c1.chair_name, c1.chair_org, c1.chair_info, c2.chair_pic_url ' \
                         'from ' \
                            'Chair c1 join ChairPic c2 ' \
                         'on ' \
                            '(c1.chair_id=c2.chair_id) ' \
                         'where ' \
                            'c1.chair_id=%s'


CHAIR_INFO_BY_SESSION = 'select distinct ' \
                            'c1.chair_id, c1.chair_name, c1.chair_org, c2.chair_pic_url ' \
                        'from ' \
                            '(Chair c1 join ChairPic c2 ' \
                            'on ' \
                            '(c1.chair_id=c2.chair_id)) left join Mange_Chair_Conference m ' \
                        'on ' \
                            '(c1.chair_id=m.chair_id)' \
                        'where ' \
                            'm.conference_id in (select conference_id from Conference where Conference.session=%s)'

CONFERENCE_CHAIR_INFO_BY_SESSION = 'select ' \
                                'conference_id, ' \
                                'session, ' \
                                'conference_topic, ' \
                                'conference_start_time, ' \
                                'conference_end_time, ' \
                                'conference_locations, ' \
                                'chair_name ' \
                             'from ' \
                                '((Conference c1 join Mange_Chair_Conference m on c1.conference_id=m.conference_id) join Chair c2 on m.chair_id=c2.chair_id)' \
                             'where ' \
                                'session=%s'


if __name__ == '__main__':
    fr = open('/media/tensor/resource/code/PythonProject/ICSHDU/ics_hdu_backend/model/DB.py')
    for line in fr.readlines():
        print(line)


