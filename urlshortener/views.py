from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect, HttpResponseNotFound, HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Link, Stats
from .forms import UrlForm, UserRegisterForm, UserLoginForm

from django.contrib import messages
from django.contrib.auth import login, logout
# Create your views here.
from .qrcode_gen import get_qr_code


def index(request, surl=None):
    if request.method == 'POST':
        form = UrlForm(request.POST)

        if form.is_valid():
            full_url = form.cleaned_data['full_url']

            if not form.cleaned_data['is_temp']:
                link = Link.objects.create(full_url=full_url)
                # get_qr_code(link.short_url)
            else:
                now = datetime.now()
                expiration_date = now + relativedelta(months=1)
                link = Link.objects.create(full_url=full_url, expiration_date=expiration_date)
                # get_qr_code(link.short_url)

            short_url = settings.SITE_URL + "/" + link.short_url
            get_qr_code(short_url)

            return render(request, 'urlshortener/index.html', {'form': form, 'surl': short_url})
    else:
        form = UrlForm()

    return render(request, 'urlshortener/index.html', {'form': form})


# def new_short_url(request, surl):
#     return render(request, 'urlshortener/stats.html', {'surl': surl})


def shorten(request, surl):
    link = get_object_or_404(Link, pk=surl)
    if link.is_expired():
        return Http404()
    link.clicked()
    link.save()

    try:
        stats = Stats()
        stats.target = link  # request.META.get("HTTP_REFERER", "")
        stats.ip = request.META.get("REMOTE_ADDR", "")
        stats.user_agent = request.META.get("HTTP_USER_AGENT", "")
        stats.save()
    except:
        pass

    return HttpResponseRedirect(link.full_url)


def statistic(request):
    return render(request, 'urlshortener/stats.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации!')
    else:
        form = UserRegisterForm()
    return render(request, 'urlshortener/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()

    return render(request, 'urlshortener/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')
