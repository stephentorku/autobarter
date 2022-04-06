from django.contrib import admin
from .models import Advertisement, AdvertisementImage, Comment
# Register your models here.


class AdvertisementImageAdmin(admin.StackedInline):
    model = AdvertisementImage

@admin.register(Advertisement)
class PostAdmin(admin.ModelAdmin):
    inlines = [AdvertisementImageAdmin]

    class Meta:
       model = Advertisement

@admin.register(AdvertisementImage)
class AdvertisementImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Comment)