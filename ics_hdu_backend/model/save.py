from django.shortcuts import render
import simplejson
from django.http import HttpResponseRedirect
from django.db import connection, transaction
from name.models import (
	KeynoteSpeech,
	Awards,
	Importantdate,
	OrganizingCommittee,
	Pastmeeting,
	Paper,
	Seminar)
# Create your views here.
cursor = connection.cursor()
def home(request):
	return render(request,'home.html')

def KeynoteSpeechSave(request):
	
	if request.method == 'POST':
		#data = simplejson.loads(request.body)
		datetime = request.POST['ks_datetime']
		name = request.POST['ks_name']
		awards = request.POST['ks_awards']
		p_code = request.POST['ks_p_code']
		human_info = request.POST['ks_human_info']
		subsidiary_organ = request.POST['ks_subsidiary_organ']
	
	keynote_speech=KeynoteSpeech()
	keynote_speech.ks_datetime=datetime
	keynote_speech.ks_name=name
	keynote_speech.ks_awards=awards
	keynote_speech.ks_p_code=p_code
	keynote_speech.ks_human_info=human_info
	keynote_speech.ks_subsidiary_organ=subsidiary_organ
	keynote_speech.save()


	return HttpResponseRedirect('/addok/')

def AwardSave(request):
	if request.method == 'POST':
		#data = simple.loads(request.body)
		name = request.POST['a_name']
		a_context_url = request.POST['a_context_url']
		a_video_url = request.POST['a_video_url']

	awards = Awards()
	awards.name=name
	awards.a_context_url=a_context_url
	awards.a_video_url=a_video_url
	awards.save()

	return HttpResponseRedirect('/addok/')

def ImportantdateSave(request):
	if request.method == 'POST':
		#data = simple.loads(request.body)
		id_pm_year = request.POST['id_pm_year']
		id_type = request.POST['id_type']
		id_name = request.POST['id_name']
		id_date = request.POST['id_date']
		id_weight = request.POST['id_weight']#????????

	important_date = Importantdate()
	important_date.id_pm_year = id_pm_year
	important_date.id_type = id_type
	important_date.id_name = id_name
	important_date.id_weight = id_weight
	important_date.save()

	return HttpResponseRedirect('/addok/')

def OrganizingCommittee(request):
	if request.method == 'POST':
		#data = simple.loads(request.body)
		oc_start_year = request.POST['oc_start_year']
		oc_end_year = request.POST['oc_end_year']
		oc_post = request.POST['oc_post']
		oc_name = request.POST['oc_name']
		oc_subsidiary_organ = request.POST['oc_subsidiary_organ']

	origanizing_committee = OrganizingCommittee()
	origanizing_committee.oc_start_year=oc_start_year
	origanizing_committee.oc_end_year=oc_end_year
	origanizing_committee.oc_post=oc_post
	origanizing_committee.oc_name=oc_name
	origanizing_committee.oc_subsidiary_organ=oc_subsidiary_organ
	origanizing_committee.save()

	return HttpResponseRedirect('/addok/')

def PastmeetingSave(request):
	if request.method == 'POST':
		#data = simple.loads(request.body)
		pm_year=request.POST['pm_year']
		pm_location=request.POST['pm_location']

	past_meeting = Pastmeeting()
	past_meeting.pm_year=pm_year
	past_meeting.pm_location=pm_location
	past_meeting.save()
	
	return HttpResponseRedirect('/addok/')

def PaperSave(request):
	if request.method == 'POST':
		#data = simple.loads(request.body)
		p_code = request.POST['p_code']
		p_awards=request.POST['p_awards']
		p_examination_questions=request.POST['p_examination_questions']

	paper=Paper()
	paper.p_code=p_code
	paper.p_awards=p_awards
	paper.p_examination_questions=p_examination_questions
	paper.save()

	return HttpResponseRedirect('/addok/')

def SeminarSave(request):
	if request.method == 'POST':
		#data = simple.loads(request.body)
		s_name=request.POST['s_name']
		s_url=request.POST['s_url']

	seminar=Seminar()
	seminar.s_name=s_name
	seminar.s_url=s_url
	seminar.save()

	return HttpResponseRedirect('/addok/')
	
def addok(request):
	return render(request,'addok.html')


