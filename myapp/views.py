from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime


def hello(request):
   today = datetime.datetime.now().date()
   daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
   return redirect("https://www.djangoproject.com")

def morning(request):
	text = "<h1>This is Hello World! App Test</h1>"
	return HttpResponse(text)

def viewArticle(request, articleId):
   """ A view that display an article based on his ID"""
   text = "Displaying article Number : %s" %articleId
   return HttpResponse(text)
	
def viewArticles(request, year, month):
   text = "Displaying articles of : %s/%s"%(year, month)
   return HttpResponse(text)

def datamanipulation(request):
   res = ''
   
   #Filtering data:
   qs = Dreamreal.objects.filter(name = "paul")
   res += "Found : %s results<br>"%len(qs)
   
   #Ordering results
   qs = Dreamreal.objects.order_by("name")
   
   for elt in qs:
      res += elt.name + '<br>'
   
   return HttpResponse(res)

def crudops(request):
   #Creating an entry
   
   dreamreal = Dreamreal(
      website = "www.polo.com", mail = "sorex@polo.com", 
      name = "sorex", phonenumber = "002376970"
   )
   
   dreamreal.save()
   
   #Read ALL entries
   objects = Dreamreal.objects.all()
   res ='Printing all Dreamreal entries in the DB : <br>'
   
   for elt in objects:
      res += elt.name+"<br>"
   
   #Read a specific entry:
   sorex = Dreamreal.objects.get(name = "sorex")
   res += 'Printing One entry <br>'
   res += sorex.name
   
   #Delete an entry
   res += '<br> Deleting an entry <br>'
   sorex.delete()
   
   #Update
   dreamreal = Dreamreal(
      website = "www.polo.com", mail = "sorex@polo.com", 
      name = "sorex", phonenumber = "002376970"
   )
   
   dreamreal.save()
   res += 'Updating entry<br>'
   
   dreamreal = Dreamreal.objects.get(name = 'sorex')
   dreamreal.name = 'thierry'
   dreamreal.save()
   
   return HttpResponse(res)