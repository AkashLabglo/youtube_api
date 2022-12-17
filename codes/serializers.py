from rest_framework.serializers import * 
from codes.models import *



class video_ser(ModelSerializer):
    #channel = ReadOnlyField()

    class Meta:
        model = Video_Upload
        fields = [
            'id',
            'channel',
            'title', 'video', 'discretion', 'is_public', 
            'monitaion', 'is_adults', 'category', 
           
        ]
        read_only_fields = (
            'likes_count', 
            'comments_count' 
        )

class Category_ser(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class Post_ser(ModelSerializer):

    class Meta:
        model = Video_Upload
        fields = [
            'channel', 
            'title', 
            'video', 
            'discretion', 
            'likes_count', 
            'comments_count'
        ]


class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'user', 'video')    


class Comment_ser(ModelSerializer):
    channel = ReadOnlyField(source='channel.username')
    #video = HyperlinkedIdentityField(view_name='upload_edit')
    class Meta:
        model = Comments          
        fields = '__all__'

'''class comment_view_ser(ModelSerializer):
        channel = ReadOnlyField(source='channel.username')
        video = HyperlinkedIdentityField(view_name='upload_edit')
        class Meta:
            model = Comments   
            fields = '__all__'''
