from django.test import TestCase
from bashmemo_server import settings
from bookmark.models import User, Keyword


class TestBookView(TestCase):

    def test_create_bookmark(self):
        user = User.objects.create_user("test", "test!", "test")
        keyword = Keyword.objects.create(name="list")
        api_token = settings.API_ACCESS_API_KEY
        response = self.client.post(
            f"/api/bookmarks/?{api_token}",
            {
                "command": "ls -larth",
                "keywords": [keyword.name],
                "object_id": user.pk
            },
            headers={
                "Content-Type": "application/json"
            }
        )
        assert response.status_code == 201
