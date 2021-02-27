from django.shortcuts import render
from django.http import HttpResponse
from scrapyd_api import ScrapydAPI

# Create your views here.

scrapyd = ScrapydAPI('http://localhost:6800')

# Create your views here.


def crawlImdb(request):
    scrapyd.schedule(project="crawling", spider="imdb")
    return HttpResponse("Crawling is done wao")