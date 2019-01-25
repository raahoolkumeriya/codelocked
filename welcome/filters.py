import django_filters
from .models import StreamType

class StreamFilter(django_filters.FilterSet):
	title = django_filters.CharFilter(lookup_expr='icontains')
	category = django_filters.CharFilter(lookup_expr='icontains')
	class Meta:
		model = StreamType
		fields = ['title', 'category']

