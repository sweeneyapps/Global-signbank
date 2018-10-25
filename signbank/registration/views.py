"""
Views which allow users to create and activate accounts.

"""


from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
from django.middleware.csrf import get_token

from signbank.registration.forms import RegistrationForm, EmailAuthenticationForm
from signbank.registration.models import RegistrationProfile
from signbank.dictionary.models import Dataset
from django.contrib import messages
from django.template.loader import render_to_string

from datetime import date

import json

def activate(request, activation_key, template_name='registration/activate.html'):
    """
    Activates a ``User``'s account, if their key is valid and hasn't
    expired.
    
    By default, uses the template ``registration/activate.html``; to
    change this, pass the name of a template as the keyword argument
    ``template_name``.
    
    Context:
    
        account
            The ``User`` object corresponding to the account, if the
            activation was successful. ``False`` if the activation was
            not successful.
    
        expiration_days
            The number of days for which activation keys stay valid
            after registration.
    
    Template:
    
        registration/activate.html or ``template_name`` keyword
        argument.
    
    """
    activation_key = activation_key.lower() # Normalize before trying anything with it.
    account = RegistrationProfile.objects.activate_user(activation_key)
    return render(request, template_name,
                              { 'account': account,
                                'expiration_days': settings.ACCOUNT_ACTIVATION_DAYS })

def register(request, success_url=settings.URL + '/accounts/register/complete/',
             form_class=RegistrationForm, profile_callback=None,
             template_name='registration/registration_form.html'):
    """
    Allows a new user to register an account.
    
    Following successful registration, redirects to either
    ``/accounts/register/complete/`` or, if supplied, the URL
    specified in the keyword argument ``success_url``.
    
    By default, ``registration.forms.RegistrationForm`` will be used
    as the registration form; to change this, pass a different form
    class as the ``form_class`` keyword argument. The form class you
    specify must have a method ``save`` which will create and return
    the new ``User``, and that method must accept the keyword argument
    ``profile_callback`` (see below).
    
    To enable creation of a site-specific user profile object for the
    new user, pass a function which will create the profile object as
    the keyword argument ``profile_callback``. See
    ``RegistrationManager.create_inactive_user`` in the file
    ``models.py`` for details on how to write this function.
    
    By default, uses the template
    ``registration/registration_form.html``; to change this, pass the
    name of a template as the keyword argument ``template_name``.
    
    Context:
    
        form
            The registration form.
    
    Template:
    
        registration/registration_form.html or ``template_name``
        keyword argument.
    
    """
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            new_user = form.save(profile_callback=profile_callback)
            request.session['username'] = new_user.username
            request.session['first_name'] = new_user.first_name
            request.session['last_name'] = new_user.last_name
            request.session['email'] = new_user.email
            groups_of_user = [ g.name.replace('_',' ') for g in new_user.groups.all() ]
            request.session['groups'] = groups_of_user

            if hasattr(settings, 'SHOW_DATASET_INTERFACE_OPTIONS') and settings.SHOW_DATASET_INTERFACE_OPTIONS:
                list_of_datasets = request.POST.getlist('dataset[]')
                if '' in list_of_datasets:
                    list_of_datasets.remove('')
                print('requested: ', list_of_datasets)

                from django.contrib.auth.models import Group, User
                group_manager = Group.objects.get(name='Dataset_Manager')

                # send email to each of the dataset owners
                for dataset_name in list_of_datasets:
                    # the datasets are selected via a pulldown list, they should exist
                    dataset_obj = Dataset.objects.get(name=dataset_name)
                    owners_of_dataset = dataset_obj.owners.all()
                    for owner in owners_of_dataset:

                        groups_of_user = owner.groups.all()
                        if not group_manager in groups_of_user:
                            # this owner can't manage users
                            continue

                        from django.core.mail import send_mail
                        current_site = Site.objects.get_current()

                        subject = render_to_string('registration/dataset_access_email_subject.txt',
                                                   context={'dataset': dataset_name,
                                                            'site': current_site})
                        # Email subject *must not* contain newlines
                        subject = ''.join(subject.splitlines())

                        message = render_to_string('registration/dataset_access_email.txt',
                                                   context={'dataset': dataset_name,
                                                            'new_user_username': new_user.username,
                                                            'new_user_firstname': new_user.first_name,
                                                            'new_user_lastname': new_user.last_name,
                                                            'new_user_email': new_user.email,
                                                            'site': current_site})

                        # for debug purposes on local machine
                        # print('owner of dataset: ', owner.username, ' with email: ', owner.email)
                        # print('message: ', message)

                        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [owner.email])

                request.session['requested_datasets'] = list_of_datasets
            return HttpResponseRedirect(success_url)
        else:
            # error messages
            messages.add_message(request, messages.ERROR, ('Error processing your request.'))
            # for ff in form.visible_fields():
            #     if ff.errors:
            #         print('form error in field ', ff.name, ': ', ff.errors)
            #         messages.add_message(request, messages.ERROR, ff.errors)

            # create a new empty form, this deletes the erroneous fields
            # form = form_class()
    else:
        form = form_class()
    return render(request,template_name,{ 'form': form })

# a copy of the login view since we need to change the form to allow longer
# userids (> 30 chars) since we're using email addresses
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.views.decorators.cache import never_cache
from django.contrib.sites.models import Site
from django.contrib.sites.requests import RequestSite


def mylogin(request, template_name='registration/login.html', redirect_field_name='/signs/recently_added/'):
    "Displays the login form and handles the login action."

    redirect_to = request.GET[REDIRECT_FIELD_NAME] if REDIRECT_FIELD_NAME in request.GET else ''
    error_message = ''

    if request.method == "POST":
        if REDIRECT_FIELD_NAME in request.POST:
            redirect_to = request.POST[REDIRECT_FIELD_NAME]

        form = EmailAuthenticationForm(data=request.POST)
        if form.is_valid():

            #Count the number of logins
            profile = form.get_user().user_profile_user
            profile.number_of_logins += 1
            profile.save()

            #Expiry date cannot be in the past
            if profile.expiry_date != None and date.today() > profile.expiry_date:
                form = EmailAuthenticationForm(request)
                error_message = _('This account has expired. Please contact o.crasborn@let.ru.nl.')

            else:
                # Light security check -- make sure redirect_to isn't garbage.
                if not redirect_to or '//' in redirect_to or ' ' in redirect_to:
                    redirect_to = settings.LOGIN_REDIRECT_URL
                from django.contrib.auth import login
                login(request, form.get_user())
                if request.session.test_cookie_worked():
                    request.session.delete_test_cookie()

                # For logging in API clients
                if "api" in request.GET and request.GET['api'] == 'yes':
                    return HttpResponse(json.dumps({'success': 'true'}), content_type='application/json')

                return HttpResponseRedirect(redirect_to)
        else:
            if "api" in request.GET and request.GET['api'] == 'yes':
                    return HttpResponse(json.dumps({'success': 'false'}), content_type='application/json')
            error_message = _('The username or password is incorrect.')

    else:
        form = EmailAuthenticationForm(request)

    request.session.set_test_cookie()
    if Site._meta.installed:
        current_site = Site.objects.get_current()
    else:
        current_site = RequestSite(request)

    # For logging in API clients
    if request.method == "GET" and "api" in request.GET and request.GET['api'] == 'yes':
        token = get_token(request)
        return HttpResponse(json.dumps({'csrfmiddlewaretoken': token}), content_type='application/json')

    return render(request,template_name, {
        'form': form,
        REDIRECT_FIELD_NAME: settings.URL+redirect_to,
        'site': current_site,
        'site_name': current_site.name,
        'allow_registration': settings.ALLOW_REGISTRATION,
        'error_message': error_message})
mylogin = never_cache(mylogin)


