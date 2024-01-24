from django.shortcuts import render, redirect
from .forms import (
    AdvancedAuthenticationForm,
    AdvancedUserCreationForm,
    UserInfoForm,
    UserBioForm,
    UserImageForm
)
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


class Login(LoginView):
    model = User
    form_class = AdvancedAuthenticationForm
    template_name = 'users/login.html'

    def form_invalid(self, form):
        for field, error in form.errors.items():
            messages.warning(self.request, f'{error}')
            return super().form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, 'You have successfully logged in!')
        return super().form_valid(form)


def register(req):
    if req.method == 'POST':
        form = AdvancedUserCreationForm(req.POST)
        if form.is_valid():
            messages.success(req, 'Your account has been created!')
            form.save()
            return redirect('main_home')
        else:
            for field, error in form.errors.items():
                messages.warning(req, f'{error}')
    else:
        form = AdvancedUserCreationForm()
    return render(req, 'users/register.html', {'form': form})


@login_required(login_url='login')
def profile(req):
    return render(req, 'users/profile.html')

@login_required(login_url='login')
def profile_update(req):
    if req.method == 'POST':
        uinfo = UserInfoForm(req.POST, instance=req.user)
        ubio = UserBioForm(req.POST, instance=req.user.profile)
        uimg = UserImageForm(req.POST, req.FILES, instance=req.user.profile)
        if ubio.is_valid() and uinfo.is_valid() and uimg.is_valid():
            uinfo.save()
            ubio.save()
            uimg.save()
            messages.info(req, 'Your profile has been updated!')
            return redirect('profile')
        else:
            for field, error in uinfo.errors.items():
                messages.warning(req, f'{error}')
            for field, error in ubio.errors.items():
                messages.warning(req, f'{error}')
            for field, error in uimg.errors.items():
                messages.warning(req, f'{error}')
    else:
        uinfo = UserInfoForm(instance=req.user)
        ubio = UserBioForm(instance=req.user.profile)
        uimg = UserImageForm(req.FILES, instance=req.user.profile)
    data = {
        "uinfo": uinfo,
        "ubio": ubio,
        "uimg": uimg
    }
    return render(req, 'users/profile_update.html', data)