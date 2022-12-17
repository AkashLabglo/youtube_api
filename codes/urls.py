from django.urls import path, include
from codes.views import *


urlpatterns = [
    path('upload/', Video_post_list.as_view(), name = "upload"),
    path('upload/<int:pk>', Video_Edit.as_view(), name = "upload_edit"),
    #===========================
    path('posts/', Post_View.as_view(), name = 'posts'), 
    #===========================
    path('likes/', CreateDeleteLikeView.as_view(), name = 'likes'),
    path('comment/', Create_Comment_view.as_view(), name = 'comment'),
    path('comment/<int:pk>', ListUpdateDeleteCommentView.as_view(), name = 'comment_edit'),
] 






