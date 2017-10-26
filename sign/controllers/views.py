from django.shortcuts import render
#from django.template.loader import render_to_string
import json
from django.http import HttpResponse

from django.http import HttpResponse
# Create your views here.
def index(request):
	#return HttpResponse("Hello django!")
	return render(request,"index.html")
def my(request):
        lists = {"a":1,"b":2}
        return HttpResponse(json.dumps(lists), content_type="application/json")

