from django.db import models

# Create your models here.
class ArticleAttributes(models.Model):

	Author = models.CharField(max_length=20)
	Title = models.CharField(max_length=100)
	Thumbnail = models.ImageField()
	Article = models.TextField(max_length=10000)
	Date = models.DateField(auto_now=True)
	Time = models.TimeField(auto_now=True)

class HotTopicArticle(ArticleAttributes):
	pass

class TransfersArticle(ArticleAttributes):
	pass

class OfficialArticle(ArticleAttributes):
	pass