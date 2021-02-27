from django.urls import path
from movie import views

# TEMPLATE_TAGGING
app_name = 'crawler'

urlpatterns = [
    path('crawl', views.crawlImdb, name="crawl_imdb"),
]