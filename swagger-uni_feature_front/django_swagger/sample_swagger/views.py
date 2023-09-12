from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from .models import Users, Tags, Influence, Contents, Front
from .serializers import UsersDataSerializer, UsersGetRequestSerializer, FrontGetRequestSerializer, UsersPostRequestSerializer, \
    UsersPostResponseSerializer, UsersPutResponseSerializer, UsersPutRequestSerializer, FrontDataSerializer, \
    FrontPostRequestSerializer, FrontPostResponseSerializer, FrontPutResponseSerializer, FrontPutRequestSerializer
from .serializers import TagsDataSerializer, TagsPostRequestSerializer, TagsPostResponseSerializer, \
    TagsPutRequestSerializer, TagsPutResponseSerializer
from .serializers import InfluenceDataSerializer, InfluencePostRequestSerializer, InfluencePostResponseSerializer, \
    InfluencePutRequestSerializer, InfluencePutResponseSerializer
from .serializers import ContentsDataSerializer, ContentsPostRequestSerializer, ContentsPostResponseSerializer, \
    ContentsPutResponseSerializer, ContentsPutRequestSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json



# @api_view(['GET']) 데이터 읽기(Read)
@api_view(['GET'])
def getUsersDatas(request):
    datas = Users.objects.all()
    serializer = UsersDataSerializer(datas, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getTagsDatas(request):
    datas = Tags.objects.all()
    serializer = TagsDataSerializer(datas, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getInfluenceDatas(request):
    datas = Influence.objects.all()
    serializer = InfluenceDataSerializer(datas, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getContentsDatas(request):
    datas = Contents.objects.all()
    serializer = ContentsDataSerializer(datas, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getFrontDatas(request):
    datas = Front.objects.all()
    serializer = FrontDataSerializer(datas, many=True)
    return Response(serializer.data)


class SerializerView(APIView):
    permission_classes = [permissions.AllowAny]

    # 특정 데이터 읽기(Read)-현재 Users 테이블만 적용했음
    class UsersFindData(APIView):
        @swagger_auto_schema(query_serializer=UsersGetRequestSerializer, responses={"200": UsersDataSerializer(many=True)})
        def get(self, request):
            param = request.query_params.get('username', None)  # 요청에서 'param' 값을 가져옵니다.
            if param is not None:
                datas = Users.objects.filter(username=param)
            else:
                datas = Users.objects.all()
            serializer = UsersDataSerializer(datas, many=True)
            return Response(serializer.data)

    class FrontFindData(APIView):
        @swagger_auto_schema(query_serializer=FrontGetRequestSerializer, responses={"200": FrontDataSerializer(many=True)})
        def get(self, request):
            param = request.query_params.get('gender', None)  # 요청에서 'param' 값을 가져옵니다.
            if param is not None:
                datas = Front.objects.filter(gender=param)
            else:
                datas = Front.objects.all()
            serializer = FrontDataSerializer(datas, many=True)
            return Response(serializer.data)

    # PostRequestSerializer 데이터 생성(Create)
    class UsersInsertData(APIView):
        @swagger_auto_schema(request_body=UsersPostRequestSerializer, responses={"201": UsersPostResponseSerializer})
        def post(self, request):
            serializer = UsersPostRequestSerializer(data=request.data)
            if serializer.is_valid():
                Users.objects.create(
                    username=serializer.validated_data['username'],
                    email=serializer.validated_data['email'],
                    profileimg=serializer.validated_data['profileimg'],
                    actoractorfollowers=serializer.validated_data['actoractorfollowers'],
                    subscriptions=serializer.validated_data['subscriptions'],
                    sociallinks=serializer.validated_data['sociallinks'],
                    contents=serializer.validated_data['contents'],
                )
                return Response({'message': 'Data created successfully.'}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    class TagsInsertData(APIView):
        @swagger_auto_schema(request_body=TagsPostRequestSerializer, responses={"201": TagsPostResponseSerializer})
        def post(self, request):
            serializer = TagsPostRequestSerializer(data=request.data)
            if serializer.is_valid():
                Tags.objects.create(
                    name=serializer.validated_data['name'],
                    categoryname=serializer.validated_data['categoryname'],
                )
                return Response({'message': 'Data created successfully.'}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    class InfluenceInsertData(APIView):
        @swagger_auto_schema(request_body=InfluencePostRequestSerializer,
                             responses={"201": InfluencePostResponseSerializer})
        def post(self, request):
            serializer = InfluencePostRequestSerializer(data=request.data)
            if serializer.is_valid():
                Influence.objects.create(
                    name=serializer.validated_data['name'],
                    subscriber=serializer.validated_data['subscriber'],
                    views=serializer.validated_data['views'],
                    cpm=serializer.validated_data['cpm'],
                    likes=serializer.validated_data['likes'],
                    comment=serializer.validated_data['comment'],
                    community=serializer.validated_data['community'],
                    operating=serializer.validated_data['operating'],
                )
                return Response({'message': 'Data created successfully.'}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    class ContentsInsertData(APIView):
        @swagger_auto_schema(request_body=ContentsPostRequestSerializer,
                             responses={"201": ContentsPostResponseSerializer})
        def post(self, request):
            serializer = ContentsPostRequestSerializer(data=request.data)
            if serializer.is_valid():
                Contents.objects.create(
                    name=serializer.validated_data['name'],
                    url=serializer.validated_data['url'],
                    title=serializer.validated_data['title'],
                    description=serializer.validated_data['description'],
                    somenameurl=serializer.validated_data['somenameurl'],
                    upload=serializer.validated_data['upload'],
                    playtime=serializer.validated_data['playtime'],
                    crawling=serializer.validated_data['crawling'],
                    likes=serializer.validated_data['likes'],
                    comments=serializer.validated_data['comments'],
                    views=serializer.validated_data['views'],
                    shares=serializer.validated_data['shares'],
                    saVES=serializer.validated_data['saVES'],
                    subscriber=serializer.validated_data['subscriber'],
                    relatedvideos=serializer.validated_data['relatedvideos'],
                    tags=serializer.validated_data['tags'],
                )
                return Response({'message': 'Data created successfully.'}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    class FrontInsertData(APIView):
        @swagger_auto_schema(request_body=FrontPostRequestSerializer, responses={"201": FrontPostResponseSerializer})
        def post(self, request):
            serializer = FrontPostRequestSerializer(data=request.data)
            if serializer.is_valid():
                Front.objects.create(
                    categories_json=serializer.validated_data['categories_json'],
                    channelMood=serializer.validated_data['channelMood'],
                    channelPurpose=serializer.validated_data['channelPurpose'],
                    gender=serializer.validated_data['gender'],
                    interests=serializer.validated_data['interests'],
                    mbti=serializer.validated_data['mbti'],
                    videoStyle=serializer.validated_data['videoStyle'],
                )
                return Response({'message': 'Data created successfully.'}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PutRequestSerializer 데이터 수정(Update)
    class UsersUpdateData(APIView):
        @swagger_auto_schema(request_body=UsersPutRequestSerializer, responses={"200": UsersPutResponseSerializer})
        def put(self, request, id):
            try:
                # 'id'를 기반으로 특정 데이터 조회
                data = Users.objects.get(id=id)
                # PUT 요청에서 새로운 데이터 값을 가져옴
                new_data = request.data
                if 'username' in new_data:
                    data.username = new_data['username']
                if 'email' in new_data:
                    data.email = new_data['email']
                if 'profileimg' in new_data:
                    data.profileimg = new_data['profileimg']
                if 'actoractorfollowers' in new_data:
                    data.actoractorfollowers = new_data['actoractorfollowers']
                if 'subscriptions' in new_data:
                    data.subscriptions = new_data['subscriptions']
                if 'sociallinks' in new_data:
                    data.sociallinks = new_data['sociallinks']
                if 'contents' in new_data:
                    data.contents = new_data['contents']
                data.save()
                serializer = UsersPutResponseSerializer(data, many=False)
                return Response(serializer.data)
            except Users.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

    class TagsUpdateData(APIView):
        @swagger_auto_schema(request_body=TagsPutRequestSerializer, responses={"200": TagsPutResponseSerializer})
        def put(self, request, id):
            try:
                # 'id'를 기반으로 특정 데이터 조회
                data = Tags.objects.get(id=id)
                # PUT 요청에서 새로운 데이터 값을 가져옴
                new_data = request.data
                if 'name' in new_data:
                    data.name = new_data['name']
                if 'categoryname' in new_data:
                    data.categoryname = new_data['categoryname']
                data.save()
                serializer = TagsPutResponseSerializer(data, many=False)
                return Response(serializer.data)
            except Tags.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

    class InfluenceUpdateData(APIView):
        @swagger_auto_schema(request_body=InfluencePutRequestSerializer,
                             responses={"200": InfluencePutResponseSerializer})
        def put(self, request, id):
            try:
                # 'id'를 기반으로 특정 데이터 조회
                data = Influence.objects.get(id=id)
                # PUT 요청에서 새로운 데이터 값을 가져옴
                new_data = request.data
                if 'name' in new_data:
                    data.name = new_data['name']
                if 'subscriber' in new_data:
                    data.subscriber = new_data['subscriber']
                if 'views' in new_data:
                    data.views = new_data['views']
                if 'cpm' in new_data:
                    data.cpm = new_data['cpm']
                if 'likes' in new_data:
                    data.likes = new_data['likes']
                if 'comment' in new_data:
                    data.comment = new_data['comment']
                if 'community' in new_data:
                    data.community = new_data['community']
                if 'operating' in new_data:
                    data.operating = new_data['operating']
                data.save()
                serializer = InfluencePutResponseSerializer(data, many=False)
                return Response(serializer.data)
            except Influence.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

    class ContentsUpdateData(APIView):
        @swagger_auto_schema(request_body=ContentsPutRequestSerializer,
                             responses={"200": ContentsPutResponseSerializer})
        def put(self, request, id):
            try:
                # 'id'를 기반으로 특정 데이터 조회
                data = Contents.objects.get(id=id)
                # PUT 요청에서 새로운 데이터 값을 가져옴
                new_data = request.data
                if 'name' in new_data:
                    data.name = new_data['name']
                if 'url' in new_data:
                    data.url = new_data['url']
                if 'title' in new_data:
                    data.title = new_data['title']
                if 'description' in new_data:
                    data.description = new_data['description']
                if 'somenameurl' in new_data:
                    data.somenameurl = new_data['somenameurl']
                if 'upload' in new_data:
                    data.upload = new_data['upload']
                if 'playtime' in new_data:
                    data.playtime = new_data['playtime']
                if 'crawling' in new_data:
                    data.crawling = new_data['crawling']
                if 'likes' in new_data:
                    data.likes = new_data['likes']
                if 'comments' in new_data:
                    data.comments = new_data['comments']
                if 'views' in new_data:
                    data.views = new_data['views']
                if 'shares' in new_data:
                    data.shares = new_data['shares']
                if 'saVES' in new_data:
                    data.saVES = new_data['saVES']
                if 'subscriber' in new_data:
                    data.subscriber = new_data['subscriber']
                if 'relatedvideos' in new_data:
                    data.relatedvideos = new_data['relatedvideos']
                if 'tags' in new_data:
                    data.tags = new_data['tags']
                data.save()
                serializer = ContentsPutResponseSerializer(data, many=False)
                return Response(serializer.data)
            except Contents.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

    class FrontUpdateData(APIView):
        @swagger_auto_schema(request_body=FrontPutRequestSerializer, responses={"200": FrontPutResponseSerializer})
        def put(self, request, id):
            try:
                # 'id'를 기반으로 특정 데이터 조회
                data = Front.objects.get(id=id)
                # PUT 요청에서 새로운 데이터 값을 가져옴
                new_data = request.data
                if 'categories_json' in new_data:
                    data.categories_json = new_data['categories_json']
                if 'channelMood' in new_data:
                    data.channelMood = new_data['channelMood']
                if 'channelPurpose' in new_data:
                    data.channelPurpose = new_data['channelPurpose']
                if 'gender' in new_data:
                    data.gender = new_data['gender']
                if 'interests' in new_data:
                    data.interests = new_data['interests']
                if 'mbti' in new_data:
                    data.mbti = new_data['mbti']
                if 'videoStyle' in new_data:
                    data.videoStyle = new_data['videoStyle']

                data.save()
                serializer = FrontPutResponseSerializer(data, many=False)
                return Response(serializer.data)
            except Front.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

    # 데이터 삭제(Delete)
    class UsersDeleteData(APIView):
        @swagger_auto_schema(responses={"204": "No Content", "404": "Not Found"})
        def delete(self, request, id):
            try:
                # 'id'를 기반으로 특정 데이터 조회
                data = Users.objects.get(id=id)
                data.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Users.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

    class TagsDeleteData(APIView):
        @swagger_auto_schema(responses={"204": "No Content", "404": "Not Found"})
        def delete(self, request, id):
            try:
                # 'id'를 기반으로 특정 데이터 조회
                data = Tags.objects.get(id=id)
                data.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Users.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

    class InfluenceDeleteData(APIView):
        @swagger_auto_schema(responses={"204": "No Content", "404": "Not Found"})
        def delete(self, request, id):
            try:
                # 'id'를 기반으로 특정 데이터 조회
                data = Influence.objects.get(id=id)
                data.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Influence.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

    class ContentsDeleteData(APIView):
        @swagger_auto_schema(responses={"204": "No Content", "404": "Not Found"})
        def delete(self, request, id):
            try:
                # 'id'를 기반으로 특정 데이터 조회
                data = Contents.objects.get(id=id)
                data.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Contents.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

    class FrontDeleteData(APIView):
        @swagger_auto_schema(responses={"204": "No Content", "404": "Not Found"})
        def delete(self, request, id):
            try:
                # 'id'를 기반으로 특정 데이터 조회
                data = Front.objects.get(id=id)
                data.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Front.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

#Front 클라이언트 save_data
@csrf_exempt
def save_data_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # 데이터를 Front 모델로 저장
            front = Front(
                interests=data['interests'],
                channelPurpose=data['channelPurpose'],
                videoStyle=data['videoStyle'],
                channelMood=data['channelMood'],
                mbti=data['mbti'],
                gender=data['gender'],
                categories_json=data['categories_json']  # categories_json 필드에 직접 배열을 할당
            )
            front.save()
            return JsonResponse({'message': '데이터가 성공적으로 저장되었습니다.'}, status=200)
        except Exception as e:
            return JsonResponse({'error': '데이터 저장 중 오류가 발생했습니다.'}, status=500)
