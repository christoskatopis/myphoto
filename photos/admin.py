from django.contrib import admin
from django.contrib import messages

from .models import Photo,Comment


class PhotoModelAdmin (admin.ModelAdmin):
  list_display = ["title","timestamp","updated"]
  list_display_links=["updated"]
  list_filter=["timestamp"]
  search_fields=["title"]


  class Meta:
  	model = Photo


class CommentAdmin(admin.ModelAdmin):
 list_display=["author","created_date","text","photo"]
 list_display_links=["author"]
 search_fields=["author"]

 class Meta:
 	model=Comment


admin.site.register(Photo,PhotoModelAdmin)
admin.site.register(Comment,CommentAdmin)
