from django.test import TestCase
from welcome.models import StreamType
from django.utils import timezone

class TestStreamType(TestCase):
    def test_stream_creation(self):
        stream = StreamType.objects.create(
            title = "Test object",
            summary = "The long summary of test object",
            category = "other",
            description = "Full description of test",
            github = "test@github.git",
            created = timezone.now(),
            tags = 'PY'
        )
        self.assertLess(stream.created, timezone.now())