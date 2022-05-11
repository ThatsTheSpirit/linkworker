from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect, HttpResponseNotFound, HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Link
from .forms import UrlForm


# Create your views here.
from .qrcode_gen import get_qr_code


def index(request, surl=None):
    if request.method == 'POST':
        form = UrlForm(request.POST)

        if form.is_valid():
            full_url = form.cleaned_data['full_url']

            if not form.cleaned_data['is_temp']:
                link = Link.objects.create(full_url=full_url)
                get_qr_code(link.short_url)
            else:
                now = datetime.now()
                expiration_date = now + relativedelta(months=1)
                link = Link.objects.create(full_url=full_url, expiration_date=expiration_date)
                get_qr_code(link.short_url)

            return render(request, 'urlshortener/new_short_url.html', {'surl': link.short_url})
            # return render(request, 'urlshortener/new_short_url.html', {'surl': link.short_url})

        else:
            return render(request, '<h1>Error</h1>')

    else:
        form = UrlForm()

    return render(request, 'urlshortener/index.html', context={'form': form})


def new_short_url(request, surl):
    return render(request, 'urlshortener/new_short_url.html', {'surl': surl})
    # return render(request, 'urlshortener/new_short_url.html')


def shorten(request, surl):
    link = get_object_or_404(Link, pk=surl)
    if link.is_expired():
        return Http404()
    link.clicked()
    link.save()
    return HttpResponsePermanentRedirect(link.full_url)


def statistic(request, surl):
    return render(request, 'urlshortener/statistic.html', {'surl': surl})
