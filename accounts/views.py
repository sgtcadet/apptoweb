from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from .models import CustomUser
from .import forms

# Create your views here.

User = get_user_model()


def registration_view(request):
    if request.method == 'POST':
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():

            user = form.save(commit=False)
            # TODO generate &/ send user authorization code
            user.auth_number = 12345
            user.save()
            # COMPLETED register & login user
            login(request, user)
            return redirect('accounts:authorization')
    else:
        form = forms.CustomUserCreationForm()
    return render(request, 'accounts/registration.html', {'form': form})


@login_required(login_url="/accounts/registration/")
def authorization_view(request):
    # TODO return 1 uppon success 0 if fail
    if request.method == 'POST':
        form = forms.CustomUserAuthorizationForm(request.POST)

        if form.is_valid():
            form_auth_number = form.cleaned_data['auth_number']
            form_email = form.cleaned_data['email']

            # Get user in DB with request email
            user = User.objects.get(email=form_email)

            # Check if user is already authorized
            if user.is_authorized:
                # return HttpResponse('User Already Authorized')
                return JsonResponse({'success': 1})
            else:
                if form_auth_number == user.auth_number:

                    # authorize the user
                    user.is_authorized = True
                    user.save()
                    # return HttpResponse('Now Authorized')
                    return JsonResponse({'success': 1})
                    # test line | return HttpResponse(user.is_authorized) returned True
                else:
                    # return HttpResponse('Error no match') # Redirect user to auth page
                    return JsonResponse({'success': 0})
            # test line | return HttpResponse(form_email)

        # test line | return HttpResponse('Request came in')
    else:
        curr_user_email = request.user.email
        form = forms.CustomUserAuthorizationForm(initial={'email': curr_user_email})
        return render(request, 'accounts/authorization.html', {'form': form})
