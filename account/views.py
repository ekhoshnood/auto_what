from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm


def registration_view(request):
    context = {}

    # if the form is post request then if there is no issue then save it and ...
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            # get the data from a valid form  =>
                                # we refrence the form the cleaned_data =>
                                                            # then get the parameter
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')

            # create the account
            account = authenticate(email = email, password = raw_password)

            # now that we have that user object
                     # then we can call login
            login(request, account)

            # after login rediret to home
                # where is home ? => in home directory(auto_what) urls we have named home the path
                                                                            # [path('', home_screen, name="home"),]
            return redirect('home')

        # if the form is not valid
        else:
            context['registration_form'] = form

    # if the request is not a post request so its get request so
                            # that means they are visiting registration form for the first time
    else:
        form = RegistrationForm()
        context['registration_form'] = form

    return render(request, 'account/register.html', context)










