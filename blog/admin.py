from django.contrib import admin
from .models import Post
from .models import Profile
from .models import Event
from .models import GalleryPhoto
from .models import Staff


admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Event)
admin.site.register(GalleryPhoto)
admin.site.register(Staff)
