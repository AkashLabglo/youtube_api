from datetime import * # datetime
from django.db.models import * # Model
from django.contrib.auth.models import User
from account.models import Create_Channel # --- > Local Another App's Model


class DateTimeUpdated(Model):
    created_at = DateTimeField(auto_now_add=True, editable=False)
    updated_at = DateTimeField(auto_now=True, editable=False)
    class Meta:
        abstract = True
#==================================================
class Category(Model):
    category = CharField(max_length=500)

    def __str__(self):
        return "{}".format(self.category)
#==================================================
class Video_Upload(DateTimeUpdated):
    channel = ForeignKey(Create_Channel, on_delete=CASCADE)
    title = CharField(max_length=500, null=True)
    category = ForeignKey(Category, on_delete=CASCADE)
    video  = FileField(upload_to="media", null= True)
    discretion = TextField(null=True)
    likes_count = IntegerField(default=0, null=False, blank=False)
    comments_count = IntegerField(default=0, null=False, blank=False)
    is_public = BooleanField(default=False, 
    help_text="0-Public, 1-Private"
    )
    monitaion =    BooleanField(default=False, 
    help_text="0-Off, 1-On"
    )
    is_adults = IntegerField(
        default=0, 
        null=False, 
        blank=False, 
        help_text="(0-All), (1-adults), (2-Kids)"
        )
    def __str__(self):
        return "{}|{}".format(self.title, self.category.category)      
#==================================================
class Post(Model):
    posts = ForeignKey(Video_Upload, on_delete=CASCADE)
    
    def __str__(self):
        return "{}|{}".format(self.posts.title, self.posts.channel.username)
#==================================================

class Like(DateTimeUpdated):
    video = ForeignKey(Video_Upload,on_delete=CASCADE,)
    user = ForeignKey(Create_Channel,on_delete=CASCADE, )

    def __str__(self):
        return "{}|{}".format(self.video.title, self.user.username)
#==================================================

class Comments(DateTimeUpdated):
     channel = ForeignKey(Create_Channel, DO_NOTHING)
     video = ForeignKey(Video_Upload,on_delete=CASCADE, related_name='comment')
     comment = CharField(max_length=500, null=True)
     is_public = BooleanField(default=False, 
     help_text="0-Public, 1-Private"
     )
     def __str__(self):
         return "{}|{}".format(self.video.title, self.comment)
#==================================================












