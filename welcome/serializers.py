from rest_framework import serializers
from .models import StreamType

class StreamSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model 	= StreamType
		fields	= ('id','url','title','summary','description','category')