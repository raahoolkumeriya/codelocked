from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import  StreamType 


class StreamTypeAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('title',)}
	list_display = ('title','created','tags')
	search_fields = ['title']
	list_filter = ('created',)

admin.site.register(StreamType,StreamTypeAdmin)	
admin.site.site_header = "CODE LOCKED"
admin.site.unregister(Group)
admin.site.unregister(User)