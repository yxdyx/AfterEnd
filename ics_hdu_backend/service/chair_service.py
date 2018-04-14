from ics_hdu_backend.models import Chair
import time


class Chairsave(object):
    def __init__(self, request):
        self.chair_name = request.POST['chair_name']
        self.chair_org = request.POSTdata['chair_org']
        self.chair_info = request.POST['chair_info']

    def addOrupdatetime(self):
        """

		:return:
		"""
        chair = Chair()
        self.add_time = time.strftime('%Y-%m-%d')
        self.obj = chair.object.filter(chair_name=self.chair_name)
        if self.obj.chair_add_time is None:
            self.obj.chair_add_time = self.add_time
            self.obj.save()
        else:
            self.obj.chair_update_time = self.add_time
            self.obj.save()

    def savechair(self):
		"""

		:return:
		"""
		chair = Chair()
		chair.chair_name = self.chair_name
		chair.chair_org = self.chair_org
		chair.chair_info = self.chair_info
		chair.save()
