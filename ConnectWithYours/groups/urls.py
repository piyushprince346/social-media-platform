from django.urls import path

from groups import views

app_name = 'groups'
urlpatterns = [
    path('filter/',views.GroupFilter,name = 'group_filter'),
    path('group_list/',views.GroupListView.as_view(),name = 'group_list'),
    path('group_details/<slug>/',views.GroupDetailView.as_view(),name = 'group_details'),
    path('group_create/',views.CreateGroupView.as_view(),name = 'create_group'),
    path('<slug>/leave/',views.LeaveGroup.as_view(),name = 'leave_group'),
    path('<slug>/join/',views.JoinGroup.as_view(),name = 'join_group'),
    path('group_list/self/',views.MyGroups.as_view(),name = 'joined_groups')
]
