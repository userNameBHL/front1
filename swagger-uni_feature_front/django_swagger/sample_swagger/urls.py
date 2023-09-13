from django.urls import path
from sample_swagger.views import SerializerView
from . import views

urlpatterns = [
        #Users
        path('v1/Users/', SerializerView.UsersInsertData.as_view(), name='users_insert_data'),
        path('v1/Users/data/', SerializerView.UsersFindData.as_view(), name='users_data'),
        path('v1/Users/update/<int:id>/', SerializerView.UsersUpdateData.as_view(), name='users_update_data'),
        path('v1/Users/delete/<int:id>/', SerializerView.UsersDeleteData.as_view(), name='users_delete_data'),
        path('v1/Users/datas/', views.getUsersDatas, name="users_datas"),

        #Tags
        path('v1/Tags/datas/', views.getTagsDatas, name="tags_datas"),
        path('v1/Tags/', SerializerView.TagsInsertData.as_view(), name='tags_insert_data'),
        path('v1/Tags/update/<int:id>/', SerializerView.TagsUpdateData.as_view(), name='tags_update_data'),
        path('v1/Tags/delete/<int:id>/', SerializerView.TagsDeleteData.as_view(), name='tags_delete_data'),

        #Influence
        path('v1/Influence/datas/', views.getInfluenceDatas, name="influence_datas"),
        path('v1/Influence/', SerializerView.InfluenceInsertData.as_view(), name='influence_insert_data'),
        path('v1/Influence/update/<int:id>/', SerializerView.InfluenceUpdateData.as_view(), name='influence_update_data'),
        path('v1/Influence/delete/<int:id>/', SerializerView.InfluenceDeleteData.as_view(), name='influence_delete_data'),

        #Contents
        path('v1/Contents/datas/', views.getContentsDatas, name="contents_datas"),
        path('v1/Contents/data/', SerializerView.ContentsFindData.as_view(), name='contents_data'),
        path('v1/Contents/', SerializerView.ContentsInsertData.as_view(), name='contents_insert_data'),
        path('v1/Contents/update/<int:id>/', SerializerView.ContentsUpdateData.as_view(), name='contents_update_data'),
        path('v1/Contents/delete/<int:id>/', SerializerView.ContentsDeleteData.as_view(), name='contents_delete_data'),

        #Front
        path('v1/Front/datas/', views.getFrontDatas, name="front_datas"),
        path('v1/Front/', SerializerView.FrontInsertData.as_view(), name='front_insert_data'),
        path('v1/Front/update/<int:id>/', SerializerView.FrontUpdateData.as_view(), name='front_update_data'),
        path('v1/Front/delete/<int:id>/', SerializerView.FrontDeleteData.as_view(), name='front_delete_data'),
        path('v1/Front/data/', SerializerView.FrontFindData.as_view(), name='front_data'),
        path('save_data/', views.save_data_view, name='save_data'),
        path('gpt/', views.gpt, name='gpt'),  # /gpt/ URL 패턴을 gpt 뷰와 연결

]