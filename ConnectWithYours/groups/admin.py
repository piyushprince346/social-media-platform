from django.contrib import admin

from .models import Group,GroupMember
# Register your models here.

class GroupMemberInline(admin.TabularInline):
    model = GroupMember # no need to register separately Group -> Groupmember


admin.site.register(Group)
