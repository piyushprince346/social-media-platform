from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse_lazy
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView

from django.contrib import messages

# Create your views here.

class ThanksView(TemplateView):
    template_name = 'accounts/thanks.html'

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password1')
            print(username)
            print(pwd)
            print('User successfully created')

            messages.success(request,"Congrats! {}, Your account has been successfully created, login to enjoy our services".format(username))
            return redirect('accounts:login')
        else:
            username = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password1')
            print(username)
            print("Invalid form")
            messages.error(request, ('Please correct the error below.'))
    else:
        form = UserRegisterForm()

    return render(request,'accounts/register.html',{'form' : form})


@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, (
                'Your profile was successfully updated!'))
            username_new = user_form.cleaned_data.get('username')
            return redirect('posts:all_post_group')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'accounts/profile_update.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

