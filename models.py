from django.db import models
from Music import settings

class Singer(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40, blank=True)
	def __str__(self):
		return u'%s %s' % (self.first_name, self.last_name)
	
class Song(models.Model):
	title = models.CharField(max_length=100)
	singer = models.ForeignKey(Singer)
	genre = models.CharField(max_length=50, blank=True)
	cover_image = models.ImageField(upload_to = u'.../static/music/cover/', blank=True) #change static URL
	audio_file = models.FileField(upload_to = u'.../static/music/mp3/', max_length=200) #change static URL
	lyrics = models.TextField(max_length=10000, blank=True)
	video_url = models.CharField(max_length=500, blank=True)
	def filename(self):
		return os.path.basename(self.audio_file.name)
