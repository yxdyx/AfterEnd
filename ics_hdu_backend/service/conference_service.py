from ics_hdu_backend.models import  Conference

class ConferenceSave(object):
	def __init__(self,request):
		
		self.session = request.POST['session']
		self.conference_topic = request.POST['conference_topic']
		self.conference_start_time = request.POST['conference_start_time']
		self.conference_end_time = request.POST['conference_end_time']
		self.conference_locations = request.POST['conference_locations']

	def saveconference(self):
		'''
		存储数据
		'''
		conference = Conference()
		conference.session = self.session
		conference.conference_topic = self.conference_topic
		conference.conference_start_time = self.conference_start_time
		conference.conference_end_time = self.conference_end_time
		conference.conference_locations = self.conference_locations
		conference.save()