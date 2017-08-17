# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Query(models.Model):
	question = models.TextField()
	dateCreated = models.DateTimeField(auto_now_add=True)
	keyword = models.TextField()

	
	def __str__(self):
		return self.question

	def response(self):
		if(question.contains("question")):
			return answer


