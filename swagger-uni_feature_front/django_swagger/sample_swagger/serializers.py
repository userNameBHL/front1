from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Users, Front
from .models import Tags
from .models import Influence
from .models import Contents


#데이터 읽기(Read)
class UsersDataSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
class TagsDataSerializer(ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'
class InfluenceDataSerializer(ModelSerializer):
    class Meta:
        model = Influence
        fields = '__all__'
class ContentsDataSerializer(ModelSerializer):
    class Meta:
        model = Contents
        fields = '__all__'
class FrontDataSerializer(ModelSerializer):
    class Meta:
        model = Front
        fields = '__all__'


#특정 데이터 읽기(Read)
class GetRequestSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
class GetResponseSerializer(serializers.Serializer):
    status = serializers.CharField()
    message = serializers.CharField()




# PostRequestSerializer 데이터 생성(Create)
class UsersPostRequestSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)
    profileimg = serializers.CharField(max_length=255)
    actoractorfollowers = serializers.CharField(max_length=255)
    subscriptions = serializers.CharField(max_length=255)
    sociallinks = serializers.CharField(max_length=255)
    contents = serializers.CharField(max_length=255)
class TagsPostRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    categoryname = serializers.CharField(max_length=255)
class InfluencePostRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    subscriber = serializers.CharField(max_length=255)
    views = serializers.CharField(max_length=255)
    cpm = serializers.CharField(max_length=255)
    likes = serializers.CharField(max_length=255)
    comment = serializers.CharField(max_length=255)
    community = serializers.CharField(max_length=255)
    operating = serializers.CharField(max_length=255)
class ContentsPostRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)
    url = serializers.CharField(max_length=255)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    somenameurl = serializers.CharField(max_length=255)
    upload = serializers.CharField(max_length=255)
    playtime = serializers.CharField(max_length=255)
    crawling = serializers.CharField(max_length=255)
    likes = serializers.CharField(max_length=255)
    comments = serializers.CharField(max_length=255)
    views = serializers.CharField(max_length=255)
    contents = serializers.CharField(max_length=255)
    shares = serializers.CharField(max_length=255)
    saVES = serializers.CharField(max_length=255)
    subscriber = serializers.CharField(max_length=255)
    relatedvideos = serializers.CharField(max_length=255)
    tags = serializers.CharField(max_length=255)

class FrontPostRequestSerializer(serializers.Serializer):
    categories_json = serializers.JSONField()
    channelMood = serializers.CharField(max_length=255)
    channelPurpose = serializers.CharField(max_length=255)
    gender = serializers.CharField(max_length=255)
    interests = serializers.CharField(max_length=255)
    mbti = serializers.CharField(max_length=255)
    videoStyle = serializers.CharField(max_length=255)



# PostResponseSerializer 데이터 생성(Create)
class UsersPostResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    email = serializers.CharField()
    profileimg = serializers.CharField()
    actoractorfollowers = serializers.CharField()
    subscriptions = serializers.CharField()
    sociallinks = serializers.CharField()
    contents = serializers.CharField()
class TagsPostResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    categoryname = serializers.CharField()
class InfluencePostResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    subscriber = serializers.CharField()
    views = serializers.CharField()
    cpm = serializers.CharField()
    likes = serializers.CharField()
    comment = serializers.CharField()
    community = serializers.CharField()
    operating = serializers.CharField()
class ContentsPostResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    url = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    somenameurl = serializers.CharField()
    upload = serializers.CharField()
    playtime = serializers.CharField()
    crawling = serializers.CharField()
    likes = serializers.CharField()
    comments = serializers.CharField()
    views = serializers.CharField()
    shares = serializers.CharField()
    saVES = serializers.CharField()
    subscriber = serializers.CharField()
    relatedvideos = serializers.CharField()
    tags = serializers.CharField()
class FrontPostResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    categories_json = serializers.JSONField()
    channelMood = serializers.CharField()
    channelPurpose = serializers.CharField()
    gender = serializers.CharField()
    interests = serializers.CharField()
    mbti = serializers.CharField()
    videoStyle = serializers.CharField()



# PutRequestSerializer 데이터 수정(Update)
class UsersPutRequestSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)
    profileimg = serializers.CharField(max_length=255)
    actoractorfollowers = serializers.CharField(max_length=255)
    subscriptions = serializers.CharField(max_length=255)
    sociallinks = serializers.CharField(max_length=255)
    contents = serializers.CharField(max_length=255)
class TagsPutRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    categoryname = serializers.CharField(max_length=255)
class InfluencePutRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    subscriber = serializers.CharField(max_length=255)
    views = serializers.CharField(max_length=255)
    cpm = serializers.CharField(max_length=255)
    likes = serializers.CharField(max_length=255)
    comment = serializers.CharField(max_length=255)
    community = serializers.CharField(max_length=255)
    operating = serializers.CharField(max_length=255)
class ContentsPutRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    url = serializers.CharField(max_length=255)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    somenameurl = serializers.CharField(max_length=255)
    upload = serializers.CharField(max_length=255)
    playtime = serializers.CharField(max_length=255)
    crawling = serializers.CharField(max_length=255)
    likes = serializers.CharField(max_length=255)
    comments = serializers.CharField(max_length=255)
    views = serializers.CharField(max_length=255)
    shares = serializers.CharField(max_length=255)
    saVES = serializers.CharField(max_length=255)
    subscriber = serializers.CharField(max_length=255)
    relatedvideos = serializers.CharField(max_length=255)
    tags = serializers.CharField(max_length=255)
class FrontPutRequestSerializer(serializers.Serializer):
    categories_json = serializers.JSONField()
    channelMood = serializers.CharField(max_length=255)
    channelPurpose = serializers.CharField(max_length=255)
    gender = serializers.CharField(max_length=255)
    interests = serializers.CharField(max_length=255)
    mbti = serializers.CharField(max_length=255)
    videoStyle = serializers.CharField(max_length=255)



# PutResponseSerializer 데이터 수정(Update)
class UsersPutResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    email = serializers.CharField()
    profileimg = serializers.CharField()
    actoractorfollowers = serializers.CharField()
    subscriptions = serializers.CharField()
    sociallinks = serializers.CharField()
    contents = serializers.CharField()
class TagsPutResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    categoryname = serializers.CharField()
class InfluencePutResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    subscriber = serializers.CharField()
    views = serializers.CharField()
    cpm = serializers.CharField()
    likes = serializers.CharField()
    comment = serializers.CharField()
    community = serializers.CharField()
    operating = serializers.CharField()
class ContentsPutResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    url = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    somenameurl = serializers.CharField()
    upload = serializers.CharField()
    playtime = serializers.CharField()
    crawling = serializers.CharField()
    likes = serializers.CharField()
    comments = serializers.CharField()
    views = serializers.CharField()
    shares = serializers.CharField()
    saVES = serializers.CharField()
    subscriber = serializers.CharField()
    relatedvideos = serializers.CharField()
    tags = serializers.CharField()
class FrontPutResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    categories_json = serializers.JSONField()  # 수정된 필드 이름
    channelMood = serializers.CharField()
    channelPurpose = serializers.CharField()
    gender = serializers.CharField()
    interests = serializers.CharField()
    mbti = serializers.CharField()
    videoStyle = serializers.CharField()
