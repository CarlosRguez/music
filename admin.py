from django.contrib import admin
from Music.music.models import Singer, Song

class SingerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'singer')
    search_fields = ('title',)
    
admin.site.register(Singer, SingerAdmin)
admin.site.register(Song, SongAdmin)
