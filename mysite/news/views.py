from django.shortcuts import render
from django.http import HttpResponse
from news.models import News

# Create your views here.
def index(request):
    news = News.objects.all()
    return render(request, 'news/index.html', {'news': news, 'title': 'Список новостей'})






# def index(request):
#     news = News.objects.all()
#     res = '<h1>Список новостей</h1>'
#     for item in news:
#         res += f"<div>\n<p>{item.title}</p>\n<p>{item.content}</p>\n</div>\n<hr>\n"
#     return HttpResponse(res)

# def test(request):
#     return HttpResponse('<h1>test page</h1>')