# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def post_home(request):
	return HttpResponse("<h1>Hello</h1>")

def post_create(request):
	return HttpResponse("<h1>Create</h1>")

def post_detail(request): #retrieve
	return HttpResponse("<h1>Detail</h1>")

def post_list(request): #list
	return render(request, 'index.html')
#	return HttpResponse("<h1>list</h1>")

def post_update(request): #retrieve
	return HttpResponse("<h1>post_update</h1>")

def post_delete(request): #retrieve
	return HttpResponse("<h1>delete</h1>")
