from django.contrib import admin
from django.urls import path, include
from account.views import *
from codes.views import *
from rest_framework.routers import DefaultRouter

url = DefaultRouter()
url.register(r'Register', Register, basename='register')
url.register(r'category', Category_view_Edits, basename='category')
#url.register(r'channel', Is_Channel, basename='channel')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('login/', Login.as_view(), name='login'),
    path('reg_update/', Is_Channel.as_view(), name='reg_update'),    
    #===========================
    path('codes/', include('codes.urls')), 



    # path('upload/', Video_post_list.as_view(), name = "upload"),
    # path('upload/<int:pk>', Video_Edit.as_view(), name = "upload_edit"),
    # #===========================
    # path('posts/', Post_View.as_view(), name = 'posts'), 
    # #===========================
    # path('likes/', CreateDeleteLikeView.as_view(), name = 'likes'),
    # path('comment/', Create_Comment_view.as_view(), name = 'comment'),
    # path('comment/<int:pk>', ListUpdateDeleteCommentView.as_view(), name = 'comment_edit'),
] 

urlpatterns += url.urls