from django.db import models
from mongoengine import Document  
   
class News(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    theme_id =models.IntegerField()
    class Meta:
        ordering = ('created',)
    def __unicode__(self):
        return self.title

class NewsDetail(models.Model):
    news = models.ForeignKey(News)
    created = models.DateTimeField(auto_now_add=True)
    content  = models.CharField(max_length=1000)
    image = models.CharField(max_length=99)
    class Meta:
        ordering = ('created',)
    def __unicode__(self):
        return self.news.title
