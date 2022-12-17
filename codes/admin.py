from django.contrib.admin import site
from codes.models import *


site.register(Category)
site.register(Video_Upload)
site.register(Post)
site.register(Like)
site.register(Comments)