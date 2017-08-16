from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
# Create your views here.

def index(request):
	#return HttpResponse("Hello django!")
	return render(request,"index.html")

def login_action(request):
	if request.method == 'POST':
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		user = auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			#return render(request,'event_manage.html')
			response = HttpResponseRedirect('/event_manage/')
			# response.set_cookie('user',username,3600)  # 添加浏览器cookie
			request.session['user'] = username  # 将session信息记录到浏览器
			return response
		else:
			return render(request,'index.html',{'error':'username or password error !'})
@login_required
def event_manage(request):
	# user = request.COOKIES.get('user','')  # 从cookie中读取信息
	user = request.session.get('user','')
	return render(request,'event_manage.html',{'user':user})