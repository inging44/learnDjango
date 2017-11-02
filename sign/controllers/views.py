from django.shortcuts import render
from django.http import HttpResponse
from sign.controllers.util import JSONResponse
from sign.models import News
from sign.models import NewsDetail
from sign.serializers import NewsSerializer
from sign.serializers import NewsDetailSerializer
from rest_framework import routers, serializers, viewsets
from rest_framework.decorators import detail_route, list_route
# from rest_framework.decorators import link

def index(request):
	#return HttpResponse("Hello django!")
	return render(request, "index.html")

def my(request):
	lists = {"a": 1, "b": 2}
	return JSONResponse(lists)
	#HttpResponse(json.dumps(lists), content_type="application/json")


class NewsViewSet(viewsets.ModelViewSet):
	queryset = News.objects.all()
	serializer_class = NewsSerializer
	@list_route()
	def latest_news(self, request):
	#展示最新的10个news.
		if request.method == 'GET':
			news = News.objects.all()[:10]
			serializer = NewsSerializer(news, many=True)
			return JSONResponse(serializer.data)


class NewsDetailViewSet(viewsets.ModelViewSet):
	queryset = NewsDetail.objects.all()
	serializer_class = NewsDetailSerializer
	#@csrf_exempt
	@detail_route()  # default---get (methods=['get'])
	def news_detail(self, request, pk= None):
	#   显示某个news的内容.
		try:
			news = NewsDetail.objects.get(news_id=pk)
		except Snippet.DoesNotExist:
			return HttpResponse(status=404)

		if request.method == 'GET':
			serializer = NewsDetailSerializer(news)
			return JSONResponse(serializer.data)
