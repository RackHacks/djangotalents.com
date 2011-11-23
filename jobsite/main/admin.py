from django.contrib import admin
from main.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'country', 'looking_for_a_job')
    list_filter = ('looking_for_a_job',)

admin.site.register(UserProfile, UserProfileAdmin)
