from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.views.generic import View
from django.contrib.auth.decorators import login_required


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/register.html')

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                fullname = form.cleaned_data.get('fullname')
                email = form.cleaned_data.get('email')            
                contact = form.cleaned_data.get('contact')
                messages.success(request, f'Your account has been created you can now login')
                return redirect('login')
        else:
            form = UserRegistrationForm()
        return render(request, 'accounts/register.html', {'form': form})


@login_required
def profile (request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'accounts/profile.html', context)