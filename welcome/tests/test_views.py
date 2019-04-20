from django.test import TestCase
from welcome.models import StreamType
from django.utils import timezone
from welcome.views import LandingView
from django.urls import reverse

"""
class TestLandingView(TestCase):

    def create_instance(self, title="only a test", slug="only-a-test", summary="yes, this is only a test"):
        return StreamType.objects.create(title=title,slug="only-a-test", summary=summary, created=timezone.now())

    def test_LandingView(self):
        w = self.create_instance()
        url = reverse("only-a-test")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(w.title, resp.content)
"""