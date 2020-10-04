from django.shortcuts import redirect, render
from django.views import View
from feedparser import parse

from home.forms import SiteForm
from home.models import Site


# Create your views here.
class Index(View):
    def get(self, request):
        form = SiteForm()
        return render(request, 'home/index.html', {'form': form})

    def post(self, request):
        form = SiteForm(request.POST)

        if form.is_valid():
            site = form.save()
            site.save()

        return redirect('index')


def get_rss_fedd(url):
    feed = parse(url)
    entries = feed['entries']

    data = [(entrie['title'], entrie['link']) for entrie in entries]

    return data
