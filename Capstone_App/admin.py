from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group
from django.core.paginator import Paginator

from Capstone_App.models import *

admin.site.unregister(Group)


@admin.register(sign_up)
class user_admin(admin.ModelAdmin):
    list_display = ['name', 'email', 'password', ]
    list_filter = ['name']
    list_display_links = ['name']
    # readonly_fields = ('s_parent_name', 's_parent_phone', 's_kid_video_link')
    list_per_page = 15
    paginator = Paginator
    pass


admin.site.register(Video)

@admin.register(Testimonial)
class testimonial_admin(admin.ModelAdmin):
    list_display = ['person_pic', 'person', 'designation', 'testimonial']
    list_filter = ['person']
    list_display_links = ['person']
    # readonly_fields = ('s_parent_name', 's_parent_phone', 's_kid_video_link')
    list_per_page = 10
    paginator = Paginator
    pass

@admin.register(FAQ_Section)
class faq_admin(admin.ModelAdmin):
    list_display = ['faq_question', ]
    list_filter = ['faq_question']
    list_display_links = ['faq_question']
    # readonly_fields = ('s_parent_name', 's_parent_phone', 's_kid_video_link')
    list_per_page = 10
    paginator = Paginator
    pass

@admin.register(WorkPlan)
class workplan_admin(admin.ModelAdmin):
    list_display = ['workplan_title', 'workplan_sheduled', 'workplan_link', ]
    list_filter = ['workplan_title']
    list_display_links = ['workplan_title']
    # readonly_fields = ('s_parent_name', 's_parent_phone', 's_kid_video_link')
    list_per_page = 10
    paginator = Paginator
    pass

@admin.register(Team_Section)
class team_admin(admin.ModelAdmin):
    list_display = ['member_name', 'member_designation', 'member_pic', ]
    list_filter = ['member_name']
    list_display_links = ['member_name']
    # readonly_fields = ('s_parent_name', 's_parent_phone', 's_kid_video_link')
    list_per_page = 10
    paginator = Paginator
    pass
