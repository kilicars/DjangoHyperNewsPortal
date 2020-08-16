from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.conf import settings
from _collections import OrderedDict
import json
import datetime
import random


def get_news_array(filename):
    with open(filename) as news_file:
        news_array = json.load(news_file)

    return news_array

# Create your views here.
class NewsView(View):
    def get(self, request, *args, **kwargs):
        # return render(request, "news/index.html")
        return redirect("/news/")

class DetailNewsView(View):
    def get(self, request, link, *args, **kwargs):

        # with open(settings.NEWS_JSON_PATH) as news_file:
        #     news_array = json.load(news_file)

        news_array = get_news_array(settings.NEWS_JSON_PATH)

        title = ""
        text = ""
        date = None

        for news in news_array:
            if news["link"] == int(link):
                title = news["title"]
                text = news["text"]
                date = news["created"]
                break

        context = {"title": title, "text": text, "created": date}
        return render(request, "news/details.html", context=context)

        # html_str = f'<h2>{title}</h2><p>{date}</p><p>{text}</p><a href="/news/" target="_blank">News page</a>'
        # return HttpResponse(html_str)

class AllNewsView(View):
    def get(self, request, *args, **kwargs):

        # with open(settings.NEWS_JSON_PATH) as news_file:
        #    news_array = json.load(news_file)

        news_array = get_news_array(settings.NEWS_JSON_PATH)

        news_dict = {}
        query_title = request.GET.get("q")

        for news in news_array:
            date_time_obj = datetime.datetime.strptime(news["created"], '%Y-%m-%d %H:%M:%S')
            key = date_time_obj.date().strftime('%Y-%m-%d')
            if query_title is None or (query_title is not None and query_title in news["title"].lower()):
                if key not in news_dict.keys():
                    news_dict[key] = list()

                news_dict[key].append(news)

        sorted_dict = OrderedDict(sorted(news_dict.items(), reverse=True))

        context = {"sorted_dict": sorted_dict}
        return render(request, "news/news.html", context=context)

class CreateNewsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "news/create.html")

    def post(self, request, *args, **kwargs):
        title = request.POST.get("title")
        text = request.POST.get("text")
        created = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        link = random.randint(0, 100000)
        json_obj = {
            "created": created,
            "title": title,
            "text": text,
            "link": link
        }

        # with open(settings.NEWS_JSON_PATH) as news_file:
        #     news_array = json.load(news_file)

        news_array = get_news_array(settings.NEWS_JSON_PATH)

        news_array.append(json_obj)

        with open(settings.NEWS_JSON_PATH, "w") as news_file:
            json.dump(news_array, news_file)

        return redirect("/news/")
