'''
import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView

# Create your views here.

def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    return render(request, 'welcome/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def health(request):
    return HttpResponse(PageView.objects.count())
'''


from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import View
from .models import StreamType
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from .forms import CommentForm
from rest_framework import viewsets
from welcome.serializers import StreamSerializer
from welcome.filters import StreamFilter

import random

class StreamView(viewsets.ModelViewSet):
	queryset = StreamType.objects.all()
	serializer_class = StreamSerializer
	
	
def LandingView(request, slugcatergory):
	nav_items=['scripting','automation','machine_learning','other']
	queryset=StreamType.objects.all()
	
	#-------------------- random projects ---------------------- #
	random_project=[]
	count_ = StreamType.objects.all().count()
	for i in range(1,30):
		random_project.append(StreamType.objects.get(pk=random.randint(1,count_)))

	
	#---------------------- paginator ---------------------------#
	paginator = Paginator(queryset,5)  # show 5 projects per page
	page = request.GET.get('page')
	try:
		query_set =  paginator.page(page)
	except PageNotAnInteger:
		query_set = paginator.page(1)
	except EmptyPage:
		query_set = paginator.page(paginator.num_pages)

	#--------------------- database fetch -----------------------#

	if slugcatergory == "home" :
		context = {'type': query_set, 
				'nav_items':nav_items, 
				'random': set(random_project[:30])}
		return render(request, 'home.html',context)
	elif slugcatergory in ['scripting','automation','machine_learning','other']:
		query_set=StreamType.objects.filter(category=slugcatergory)
		context = {'type': query_set , 
				'nav_items':nav_items, 
				'random': set(random_project[:30])}
		return render(request, 'home.html',context)
	elif slugcatergory == "allproject":
		context = { 'filter': StreamFilter(request.GET, queryset=queryset) , 
			  'all_datasets': queryset, 
			'nav_items':nav_items}
		return render(request, 'allproject.html',context)
	else:
		query_set=StreamType.objects.get(slug=slugcatergory)
		context = {'type': query_set , 
				'nav_items':nav_items,  
				'random': set(random_project[:30]) }
		return render(request, 'detail.html',context)
		
def error_404_view(request, exception):
    data = {"name": "CodeLocked.tk"}
    return render(request,'error_404.html', data)

