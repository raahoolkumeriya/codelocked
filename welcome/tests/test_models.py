from django.test import TestCase
from welcome.models import StreamType
from django.utils import timezone

class TestStreamType(TestCase):
    def create_instance(self, title="only a test", summary="yes, this is only a test"):
        return StreamType.objects.create(title=title, summary=summary, created=timezone.now())

    def test_instance_creation(self):
        w = self.create_instance()
        self.assertTrue(isinstance(w, StreamType))
        self.assertEqual(w.__str__(), w.title)