
'''
from django.contrib import admin
from .models import PageView

# Register your models here.


class PageViewAdmin(admin.ModelAdmin):
    list_display = ['hostname', 'timestamp']

admin.site.register(PageView, PageViewAdmin)
'''

from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import  StreamType 


class StreamTypeAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('title',)}
	list_display = ('title','created','tags')
	search_fields = ['title','tags']
	list_filter = ('created',)

admin.site.register(StreamType,StreamTypeAdmin)	
admin.site.site_header = "CODE LOCKED"
admin.site.unregister(Group)
admin.site.unregister(User)