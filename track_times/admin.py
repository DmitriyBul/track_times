from django.contrib import admin

from track_times.models import UserTime, UserActivity

'''
@admin.register(UserTime)
class UserTimeAdmin(admin.ModelAdmin):
    list_display = ['user', 'start', 'end']
    list_filter = ['user', 'start', 'end']
    list_editable = ['start', 'end']
'''


@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'start', 'end']
    list_filter = ['user', 'title', 'start', 'end']
    list_editable = ['title', 'start', 'end']
