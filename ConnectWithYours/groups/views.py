from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,RedirectView

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.urls import reverse

from .models import Group,GroupMember
# Create your views here.

@login_required
def GroupFilter(request):
    
    search = request.POST['group_name']
    groups = Group.objects.filter(name__startswith= search)

    return render(request,'groups/group_list.html',{'groups' : groups})

class MyGroups(LoginRequiredMixin,ListView):
    model = Group
    context_object_name = 'groups'
    template_name = 'groups/my_group_list.html'

class CreateGroupView(LoginRequiredMixin,CreateView):
    model = Group
    fields = ['name','description']
    template_name = 'groups/group_form.html'

class GroupDetailView(LoginRequiredMixin,DetailView):
    model = Group
    template_name = 'groups/group_details.html'

class GroupListView(LoginRequiredMixin,ListView):
    model = Group
    context_object_name = 'groups'
    template_name = 'groups/group_list.html' 

class JoinGroup(LoginRequiredMixin,RedirectView):
    def get_redirect_url(self,*args, **kwargs):
        return reverse('groups:group_details',kwargs={'slug' : self.kwargs.get('slug')})

    def get(self,request,*args, **kwargs):
        group = get_object_or_404(Group,slug = self.kwargs.get('slug'))

        try:
            GroupMember.objects.create(user = self.request.user,group = group)
        except IntegriyError:
            messages.warning(self.request,'Warning! you are alraedy a member of this group')
        else:
            messages.success(self.request,'You have successfully joined the group')

        return super().get(request,*args, **kwargs)

class LeaveGroup(LoginRequiredMixin,RedirectView):
    def get_redirect_url(self,*args, **kwargs):
        return reverse('groups:group_details', kwargs={'slug': self.kwargs.get('slug')})
    
    def get(self,request,*args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))

        try:
            membership = GroupMember.objects.filter(
                user = self.request.user,
                group = group)
        except GroupMember.DoesNotExist:
            messages.warning(self.request,'Oops, you are not the member of this group')
        else:
            membership.delete()
            messages.success(self.request,'You have successfully left the group!')
        
        return super().get(request,*args, **kwargs)



    
