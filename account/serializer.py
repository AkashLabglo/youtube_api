from rest_framework.serializers import *
from account.models import Create_Channel
#from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from django.contrib.auth.password_validation import validate_password



class Register_ser(ModelSerializer):
    password = CharField(
    style={'input_type': 'password'},
    write_only = True, 
    validators=[validate_password]
)
    token = SerializerMethodField('get_user_token')
    class Meta:
        model = Create_Channel
        fields =['id','first_name', 'last_name','email', 'username', 'password', 'is_channel', 'phone' ,'token']
        #fields = "__all__"

 
    def create(self, validated_data):
        user = Create_Channel.objects.create(
        username=validated_data['username'],
        email=validated_data['email'],
        first_name=validated_data['first_name'],
        last_name=validated_data['last_name']
        ) 
        if validated_data['is_channel']:
            user.channel_name = validated_data['last_name']
            user.phone = validated_data['phone']
            user.is_channel  = True
            user.save()
        user.set_password(validated_data['password'])
        user.save()
        return JsonResponse(user, safe=False)

    def get_user_token(self, obj):
        return Token.objects.get_or_create(user=obj)[0].key    


class Channel_Update_ser(ModelSerializer):

    class Meta:
        model= Create_Channel
        fields = [
        'username' , 
        'is_channel', 'phone' 
        ]
    #fields = "__all__"

    



class Login_ser(ModelSerializer):
    password = CharField(
    style={'input_type': 'password'},
    write_only = True, 
    validators=[validate_password]
)
    class Meta:
        model = Create_Channel
        fields = ["id",  "username", "password"]        