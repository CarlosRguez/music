from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from Carlos.music.models import Song, Singer
from Carlos import settings

def music(request):
    music = Song.objects.all()
    if not music:
        return HttpResponseRedirect('/music/')
    else:
        URL = settings.MEDIA_URL
        return render_to_response('music/music.html', {'music': music})
