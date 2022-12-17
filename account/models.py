from django.db.models import *
from django.contrib.auth.models import AbstractUser
from uuid import uuid4



class Create_Channel(AbstractUser):

    channel_name = CharField(max_length=150, null = True)
    is_channel = BooleanField(default=False, 
    help_text="0->Not_Channel, 1-> Is_channel"
    )
    phone = IntegerField(null = True)
    #token = CharField(max_length=250, unique=True, null=True)
    # def __str__(self):
    #     return self.channel_name
