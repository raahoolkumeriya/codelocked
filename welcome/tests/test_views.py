from django.test import TestCase
from welcome.models import StreamType
from django.utils import timezone
from welcome.views import LandingView
from django.urls import reverse
from django.template.defaultfilters import slugify
"""
class TestLandingView(TestCase):
    def setUp(self):
        self.stream1 = StreamType.objects.create(
            title = "Test object 1",
            summary = "The long summary of test object 1",
            category = "other",
            description = "Full description of test 1",
            github = "test1@github.git",
            created = timezone.now(),
            tags = 'PY',
            slug = 'test-object-1'
        )
        self.stream2 = StreamType.objects.create(
            title = "Test object 2",
            summary = "The long summary of test object 2",
            category = "other",
            description = "Full description of test 2",
            github = "test2@github.git",
            created = timezone.now(),
            tags = 'PY',
            slug = 'test-object-2'
        )

    def test_stream_list_view(self):
        url = slugify(self.stream1.title)
        resp = self.client.get(reverse(url))
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp, template_name='allproject.html',context=(self.stream1, self.stream2,) )
"""