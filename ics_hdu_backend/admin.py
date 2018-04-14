from django.contrib import admin

from .models import Chair
from .models import ChairPic
from .models import Conference
from .models import Manage_Chair_Conference

"""
在admin内录入主席信息/主席照片/会议信息/主席与会议关系
by: junyachen
"""
admin.site.register(Chair)
admin.site.register(ChairPic)
admin.site.register(Conference)
admin.site.register(Manage_Chair_Conference)