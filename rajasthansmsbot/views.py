# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
import os
import requests

from .models import *

# Create your views here.

API_KEY = "169279AKs6QaxtS7Fd598c2841"


@csrf_exempt
def Ask(request):
	question = request.POST.get("message", "")
	number = request.POST.get("number", "")
	keyword = request.POST	.get("keyword", "")

	q = Query(question=question, keyword=keyword)
	q.save()
	response = q.response()


	data_payload = {'authkey': API_KEY, 'mobiles': number, 'message':response,
	'country':'91','route':'4'}


	r = requests.get("https://control.msg91.com/api/sendhttp.php?",params = data_payload)
	print(r.content)
	return HttpResponse("Message recieved")
