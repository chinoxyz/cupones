__author__ = 'josegregorio'

from django.contrib.auth import login, authenticate
from django.core.urlresolvers import reverse
from django.forms.forms import NON_FIELD_ERRORS
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from .forms import LoginForm


def login(request):
    form = None
    follow = '/'
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            login_data = form.cleaned_data
            user = authenticate(username=login_data['username'], password=login_data['password'])

            if user and user.is_active:
                login(request, user)
                response = HttpResponseRedirect(reverse(follow))
                return response
            else:
                form._errors[NON_FIELD_ERRORS] = _('The username or password you entered are invalid.')

    context = {'form': form, 'next': follow}
    return render(request, 'user/login.html', context)


def register(request):
    return HttpResponse("The register view is coming soon...")


def logout(request):
    return HttpResponse("The logout view is coming soon...")


def password_reset(request):
    return HttpResponse("The password reset view is coming soon...")