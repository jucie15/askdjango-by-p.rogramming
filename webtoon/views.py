from django.shortcuts import render
from .models import Webtoon

def webtoon_list(request):
    q = request.GET.get('q', '')
    webtoon_list = Webtoon.objects.all()

    if q:
        webtoon_list = Webtoon.objects.filter(title__contains = q)

    return render(request, 'webtoon/webtoon_list.html', {'webtoon_list' : webtoon_list,
        'q' : q,
        })


def webtoon_detail(request, id):
    webtoon = Webtoon.objects.get(id = id)
    #Webtoon.objects.fileter(id = id)[0]
    return render(request, 'webtoon/webtoon_detail.html', {'webtoon' : webtoon,
        })
