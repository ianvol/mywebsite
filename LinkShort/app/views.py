from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
import hashlib
import random
from django.contrib.auth.decorators import login_required
import shortuuid
from django.contrib.auth.models import User

from .models import URL

def generate_short_url():
    # Generate a unique short URL using shortuuid
    short_url = shortuuid.uuid()[:6]  # Use the first 6 characters

    return short_url


def link_short(request):
    context = {}
    context['title'] = 'Link Shortener'

    if request.method == 'POST':
        long_url = request.POST.get('long_url')

        if long_url:
            if request.user.is_authenticated:
                user = request.user

                # Check if the long URL already exists
                existing_url = URL.objects.filter(long_url=long_url).first()

                if existing_url:
                    context['short_url'] = existing_url.short_url
                else:
                    # Generate a short URL
                    short_url = generate_short_url()

                    # Create a new URL object
                    url = URL(long_url=long_url, short_url=short_url, user=user)
                    url.save()

                    context['short_url'] = short_url
            else:
                # Get or create an anonymous user
                user, created = User.objects.get_or_create(username='anonymous')
                
                # Create a new URL object and save it to the database
                short_url = generate_short_url()
                url = URL(long_url=long_url, short_url=short_url, user=user)
                url.save()
                
                context['short_url'] = short_url

    return render(request, 'link_short.html', context)


def redirect_short_url(request, short_url):
    url = URL.objects.filter(short_url=short_url).first()

    if url:
        return redirect(url.long_url)
    else:
        return render(request, 'link_short.html', {'error': 'Invalid short URL'})


@login_required
def my_links(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user_links = URL.objects.filter(user__id=user_id)
        print(user_links) 
        return render(request, 'my_links.html', {'user_links': user_links})
    else:
        return redirect('login')


def me(request):
    context = {
        'title': 'Welcome to My App',
    }
    return render(request, 'me.html', context)

def iss(request):
    return render(request, 'iss.html')

def project_flex(request):
    return render(request, 'project_flex.html')