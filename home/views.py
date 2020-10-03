from django.shortcuts import redirect, render
from django.views import View
from feedparser import parse


# Create your views here.
class Index(View):
    def get(self, request):
        return render(request, 'home/index.html')

    def post(self, request):
        rss_site = request.POST['rss_site']
        data = get_rss_fedd(rss_site)

        return render(request, 'home/index.html', {'data': data})


def get_rss_fedd(url):
    feed = parse(url)
    entries = feed['entries']

    data = [(entrie['title'], entrie['link']) for entrie in entries]

    return data
