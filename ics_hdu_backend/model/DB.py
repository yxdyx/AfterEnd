"""

"""

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
