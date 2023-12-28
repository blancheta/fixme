from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from rest_framework.relations import RelatedField
from rest_framework.serializers import CharField, ModelSerializer

from bookmark.models import Bookmark, Keyword, User
from rest_framework.authtoken.models import Token


class KeywordsField(RelatedField):

    def to_internal_value(self, value):
        return value

    def to_representation(self, value):
        return value


class UserCreateSerializer(ModelSerializer):
    token = CharField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'token']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        token, state = Token.objects.get_or_create(user_id=instance.id)
        data["token"] = token.key
        return data


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['pk', 'organisation']


class BookmarkSerializer(ModelSerializer):
    keywords = KeywordsField(write_only=True, many=True, queryset=Keyword.objects.all())

    class Meta:
        model = Bookmark
        fields = ['command', 'keywords', 'object_id']
        depth =1

    def create(self, validated_data):
        data = validated_data.copy()
        keywords = data["keywords"]

        bookmark = Bookmark.objects.create(
            command=data["command"],
            object_id=data["object_id"],
            content_type=ContentType.objects.get(model='user')
        )
        bookmark.save()
        if "keywords" in validated_data:
            for keyword in keywords:
                bookmark.keywords.create(name=keyword)

        return bookmark
