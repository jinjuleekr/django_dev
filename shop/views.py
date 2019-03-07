from django.shortcuts import render, redirect, resolve_url
from django.template.loader import render_to_string
from django.urls.base import reverse

from .models import Article
from django.http import HttpResponse
from django.db.models import Q
from django.utils import timezone

class Person():
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        return self.name + " 안녕하세요:D"
    def __str__(self):
        return self.name+'님'


def template_test(request):
    article = Article.objects.get(id=1)
    myname = '정진'
    people = ['정표', '왕기', '아라']
    p = Person("정은")

    dt = timezone.now()

    dt = timezone.now()
    str_dt = dt.strftime("%Y-%m-%d %H:%M:%S")
    past_dt = timezone.datetime(2005,8,31)
    future_dt = timezone.datetime(2019,5,21)

    return render(request, 'shop/template_test.html',
            {'article': article, 
            'first_name':myname, 
            'people':people,
            'person':p,
            'student_list': [],
            'datetime_obj' : dt, 
            'dt':dt, 
            "sdt":str_dt, 
            "past_dt":past_dt, 
            "future_dt":future_dt
            }
            )

def template_test2(request):
    article = Article.objects.get(id=1)
    myname = '정진'
    people = ['정표', '왕기', '아라']
    p = Person("정은")
    return render(request, 'shop/template_test.html',
            {'article': article, 
            'first_name':myname, 
            'people':people,
            'person':p,
                }
            )

def article_list(request):
    qs = Article.objects.all() #qs = queryset
    q = request.GET.get('q', '') #request.getParameter('q')
    if q:
        qs = qs.filter(title__contains=q)
    return render(request, 'shop/article_list.html', 
    {'article_list':qs, 'q2':q})

def article_insert(request):
    article = Article(title='목요일', body="날씨가 좋습니다.", status='p')
    article.save()
    Article.objects.create(title='금요일', body="날씨가 안 좋습니다.", status='p')
    return HttpResponse("입력합니다.")

def article_update(request):
    aa = Article.objects.first()
    aa.title = 'Friday'
    aa.save()
    '''
    qs = Article.objects.filter(title__contains="1")
    print(qs)
    for aa in qs:
        aa.title = 'have 1'
        aa.save()
    '''
    # qs.update 일괄 업데이트시 더 유용함
    qs = Article.objects.filter(title__contains="3")
    qs.update(title = 'have 3')
    print("방법1:", qs.query)
    s = str(qs.query)
    print("방법2:", s)
    return HttpResponse("수정합니다.")

def article_delete(request):
    qs = Article.objects.filter(Q(title__contains="9") | Q(title__contains="5"))
    qs.delete()
    return HttpResponse("삭제합니다.")

def test1(request):
    response = render(request, 'shop/test1.html', {'mymessage':'render이용하기'})
    return response

def test2(request):
    s = render_to_string('shop/test1.html', {'mymessage':'render_to_string이용하기'})
    return HttpResponse(s)

def test3(request):
    if request.method == 'GET':
        response = render(request, 'shop/csrf_input.html')
        return response
    else:
        title = request.POST['title']
        body = request.POST['body']
        status = request.POST['status']
        aa = Article(title=title, body=body, status=status)
        aa.save()

        return HttpResponse("입력")

def article_detail(request, id2):
    instance = Article.objects.get(id=id2) #앞의 id는 칼럼, 뒤의 id2는 변수
    print(instance)
    return render(request, 'shop/article_detail.html', {'article':instance})

def article_reversetest(request):

    #url 만들기
    a = reverse('shop:list')
    print('shop:list와 같이 요청함: ', a)

    a = reverse('shop:detail', args=[1]) #/shop/1/detail
    print('shop:detail 같이 요청함: ', a)

    a = reverse('shop:detail', kwargs={'id2':3}) #/shop/3/detail
    print('shop:detail 같이 요청함: ', a)

    a = resolve_url('shop:detail', 249)
    
    return redirect(a)
    # return redirect('shop:list') #주소창이 바뀐다