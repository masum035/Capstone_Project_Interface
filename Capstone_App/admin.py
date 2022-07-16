from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group
from django.core.paginator import Paginator

from Capstone_App.models import *

admin.site.unregister(Group)

@admin.register(sign_up)
class user(admin.ModelAdmin):
    list_display = ['name', 'email', 'password',]
    list_filter = ['name']
    list_display_links = ['name']
    # readonly_fields = ('s_parent_name', 's_parent_phone', 's_kid_video_link')
    list_per_page = 15
    paginator = Paginator
    pass

admin.site.register(Video)

# @admin.register(Upload_File)
# class user(admin.ModelAdmin):
#     list_display = ['name', 'existingPath', 'eof',]
#     list_filter = ['name']
#     list_display_links = ['name']
#     # readonly_fields = ('s_parent_name', 's_parent_phone', 's_kid_video_link')
#     list_per_page = 15
#     paginator = Paginator
#     pass

