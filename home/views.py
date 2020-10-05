from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.list import ListView
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

        return redirect('sites')


class ListSites(ListView):
    model = Site
    queryset = Site.objects.all()
    template_name = 'home/sites.html'
    context_object_name = 'sites'


def feed_site(request, site_id):
    site = Site.objects.get(id=site_id)

    feed = get_rss_fedd(site.rss_site)

    return render(request, 'home/site_feed.html', {
        'feed': feed,
        'name': site.name
    })


class AddNewSite(View):
    def get(self, request):
        form = SiteForm()
        return render(request, 'home/new_site.html', {'form': form})

    def post(self, request):
        form = SiteForm(request.POST)

        if form.is_valid():
            site = form.save()
            site.save()

        return redirect('sites')


def get_rss_fedd(url):
    feed = parse(url)
    entries = feed['entries']

    data = [(entrie['title'], entrie['link']) for entrie in entries]

    return data
