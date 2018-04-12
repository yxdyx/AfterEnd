from django.db import models
from .utils.file_upload import Multimedia


class Chair(models.Model):
    """
    主席信息 {自动增长列：chair_id,
            主席名称：chair_name,
            主席所属机构：chair_org,
            主席信息：chair_info,
            主席信息录入时间：chair_add_time,
            主席信息更新时间：chair_update_time}
    """
    chair_id = models.AutoField(primary_key=True)
    chair_name = models.CharField(max_length=50)
    chair_org = models.CharField(max_length=255)
    chair_info = models.TextField()
    chair_add_time = models.DateField()
    chair_update_time = models.DateField()

    class Meta:
        managed = False
        db_table = 'Chair'

    def __str__(self):
        return str({'chair_id': self.chair_id,
                    'chair_name': self.chair_name,
                    'chair_org': self.chair_org,
                    'chair_info': self.chair_info})


class ChairPic(models.Model):
    """
    主席照片管理 {自动增长列：chair_pic_id,
                主席id：chair_id,
                会议年份：session,
                照片url地址：chair_pic_url}
    """
    chair_pic_id = models.AutoField(primary_key=True)
    chair_id = models.IntegerField()
    session = models.IntegerField()
    chair_pic_url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ChairPic'

    def __str__(self):
        return str({'chair_id': self.chair_id,
                    'session': self.session,
                    'chair_pic_url': self.chair_pic_url})


class Conference(models.Model):
    """
    会议信息 {会议id：conference_id,
            会议年份：session,
            会议主题：conference_topic,
            会议开始时间：conference_start_time,
            会议结束时间：conference_end_time,
            会议地点：conference_locations}
    """
    conference_id = models.AutoField(primary_key=True)
    session = models.IntegerField()
    conference_topic = models.CharField(max_length=255)
    conference_start_time = models.DateTimeField()
    conference_end_time = models.DateTimeField()
    conference_locaitons = models.CharField(max_length=512)

    class Meta:
        managed = False
        db_table = 'Conference'

    def __str__(self):
        return str({'conference_id': self.conference_id,
                    'session': self.session,
                    'conference_topic': self.conference_topic,
                    'conference_start_time': self.conference_start_time,
                    'conference_end_time': self.conference_end_time,
                    'conference_locations': self.conference_locaitons})


class Manage_Chair_Conference(models.Model):
    """
    主席与会议关系 {自动增长列：manage_id,
                 会议id：conference_id,
                 主席id：chair_id}
    """
    manage_id = models.AutoField(primary_key=True)
    conference_id = models.IntegerField()
    chair_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Manage_Chair_Conference'

    def __str__(self):
        return str({'conference_id': self.conference_id,
                    'chair_id': self.conference_id})


class User(models.Model):
    """
    用户信息 {用户id：user_id,
            用户名：user_name,
            用户邮箱：user_email,
            用户密码：user_password}
    """
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255)
    user_email = models.CharField(max_length=255)
    user_password = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'User'

    def __str__(self):
        return str({'user_id': self.user_id,
                    'user_name': self.user_name,
                    'user_email': self.user_email,
                    'user_password': self.user_password})


<<<<<<< HEAD
class Chair_img(models.Model):
    """
    数据库中主席照片信息
    """
    chair_id = models.CharField(max_length=32, default="")
    img_year = models.CharField(max_length=32, default="")
    chair_img = models.ImageField(upload_to=Multimedia.upload_to, max_length=150)
=======
# 主席照片在admin内录入
class ChairPic(models.Model):
    chair_pic_id = models.AutoField(primary_key=True)
    chair_id = models.CharField(max_length=32)
    session = models.CharField(max_length=32)
    chair_pic_url = models.ImageField(upload_to=upload_to, max_length=150)
    class Meta:
        managed = False
        db_table = 'ChairPic'
>>>>>>> c424fc4c02f975a2587acdafb469f6652c7e0347

    def __str__(self):
        return str(self.chair_id) + '/' + str(self.session)


