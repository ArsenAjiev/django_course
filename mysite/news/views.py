from django.shortcuts import render
from django.http import HttpResponse
from news.models import News, Category

# Create your views here.
def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
    }
    return render(request, template_name='news/index.html', context=context)


def get_category(request, category_id):
    news =News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'category': category,
    }
    return render(request, 'news/category.html', context=context)


# def index(request):
#     news = News.objects.all()
#     res = '<h1>Список новостей</h1>'
#     for item in news:
#         res += f"<div>\n<p>{item.title}</p>\n<p>{item.content}</p>\n</div>\n<hr>\n"
#     return HttpResponse(res)

# def test(request):
#     return HttpResponse('<h1>test page</h1>')