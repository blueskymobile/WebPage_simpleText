from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello(request):
   text = "<h1>welcome to my app number !</h1>"
   return HttpResponse(text)
def morning(request):
	text = "<h1>This is Hello World! App Test</h1>"
	return HttpResponse(text)

def viewArticle(request, articleId):
   text = "Displaying article Number : %s"%articleId
   return HttpResponse(text)