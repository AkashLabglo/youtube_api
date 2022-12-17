from django.shortcuts import render
from django.http import JsonResponse

from codes.models import *
from codes.serializers import *
from codes.permissions import(
    PublicAvailable, 
    IsOwner, IsAuthenticate
)

from rest_framework.response import Response # Rest_framework 
from rest_framework.generics import * # Rest_framework 
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import NotAcceptable
from rest_framework.exceptions import NotFound

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::
class Video_post_list(ListCreateAPIView):
    queryset = Video_Upload.objects.all()
    serializer_class = video_ser
    permission_classes = [IsOwner]
    

    def perform_create(self, serializer):
        serializer.save(channel_id = self.request.user.id)

    def list(self, request, *args, **kwargs):
        user = self.request.user.id
        opj1 = Video_Upload.objects.filter(
            channel = user
        )
        serializer = self.get_serializer(opj1, many=True)
        return Response(serializer.data)

    

class Video_Edit(RetrieveUpdateDestroyAPIView):
    serializer_class = video_ser
    permission_classes = [IsOwner]
    def get_queryset(self):
        user = self.request.user
        opj = Video_Upload.objects.filter(
            channel = user
        )
        return opj 
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Category_view_Edits(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = Category_ser

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Post_View(ListAPIView):
    queryset = Video_Upload.objects.all()
    serializer_class = Post_ser
    permission_classes = [PublicAvailable]
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()) # Queryset Access
        print(">>>>>>", queryset)
        queryset = queryset.filter(Q(is_public=False))
        print(">>>>>> @", queryset)
        for video in queryset.all():
            print("/////------>", video.likes_count)
            video_id = video.id
            likes_count = Like.objects.filter(video=video_id).count()
            print('<<<<<<<<<',video_id)
            video.likes_count = likes_count
            print("--------->", Comments.objects.filter(video=video_id).count())
            video.comments_count = Comments.objects.filter(video=video_id).count()
            video.save()

        serializer = self.get_serializer(queryset, many=True)
        print("*********", self.get_serializer)
        return Response(serializer.data)

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::

class CreateDeleteLikeView(CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [PublicAvailable]

    def perform_create(self, serializer):
        if self.request.data['user'] != str(self.request.user.id):
            raise NotAcceptable("Not authorized.")

        queryset = self.filter_queryset(self.get_queryset())
        subset = queryset.filter(Q(user_id=self.request.data['user']) & Q(video_id=self.request.data['video']))

        # If it's already liked, then just dislike.
        if subset.count() > 0:
            subset.first().delete()
            return
        serializer.save()


#:::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Create_Comment_view(ListCreateAPIView):
    queryset  = Comments.objects.all()
    serializer_class = Comment_ser
    permission_classes = [PublicAvailable]

    def perform_create(self, serializer):
        video_id = int(self.request.data['video'])
        posts = Video_Upload.objects.filter(id=video_id, is_public=False)
        print(">>>>>>>>>>", posts)
        if posts.count() != 1:
            raise NotFound()

        serializer.save(channel=self.request.user, is_public=False, video_id=video_id)
# # >>>>>>>>>>>>>>>>>>>>>>>>>> Tweet._Related -------------->

class ListUpdateDeleteCommentView(RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = Comment_ser
    permission_classes = [IsAuthenticate]
    
    def perform_update(self, serializer):
        comment_id = int(self.kwargs.get('pk'))

        queryset = self.filter_queryset(self.queryset)
        queryset = queryset.filter(Q(id=comment_id) & Q(account_owner=self.request.user))

        if queryset.count() != 1:
            raise NotFound("Comment not found.")

        comment = queryset.get()

        serializer.save(parent=comment.video, is_public=False)
# >>>>>>>>>>>>>>>>>>>>>>>>>> Tweet._Related -------------->

# skyakash_2 --> skyakash_2@123

# skyakash --> skyakash@123

