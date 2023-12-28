from django.test import TestCase

# Create your tests here.
from bookmark.models import User, Keyword
from bookmark.serializers import BookmarkSerializer


class TestBookMarkSerializer(TestCase):

    def test_bookmark_serializer(self):
        user = User.objects.create_user("test", "test!", "test")
        keyword = Keyword.objects.create(name="truc")
        bookmark_serializer = BookmarkSerializer(data={
            "object_id": user.pk,
            "keywords": ["truc"]
        })
