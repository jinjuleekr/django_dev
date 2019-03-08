from django.shortcuts import render, redirect, resolve_url, get_object_or_404
from django.template.loader import render_to_string
from django.urls.base import reverse
from .models import Article
from django.http import HttpResponse
from django.db.models import Q
from django.utils import timezone
from django.views.generic import DetailView
from django.views import View

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
            "future_dt":future_dt,
            'value':[], 'value2':None, 'value3':['a','b','c'],
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
#list view 방법 1
'''
def article_list(request):
    qs = Article.objects.all() #qs = queryset
    q = request.GET.get('q', '') #request.getParameter('q')
    if q:
        qs = qs.filter(title__contains=q)
    return render(request, 'shop/article_list.html', 
    {'article_list':qs, 'q2':q})
'''
#list view 방법 2
from django.views.generic import ListView
from django.utils import timezone

# article_list = ListView.as_view(model=Article, paginate_by=10) #/?page=3

class ArticleListView(ListView):
    model = Article
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mymessage"] = "ListView상속"
        context["today"] = timezone.now() 
        context["q2"] = self.request.GET.get('page','')
        return context

article_list = ArticleListView.as_view()

from .forms import ContactForm
from django.views.generic.edit import FormView

class ContactView(FormView):
    template_name = 'shop/contact.html'
    form_class = ContactForm
    success_url = '/shop/thanks/' #urls.py설정  #/부터 시작하면 루트부터 시작 

    # html tag들을 쓸 수 있음
    def form_valid(self, form):
        print(form)
        print(form.cleaned_data) #valid에 통과한 data
        print(form.cleaned_data['name'])
        print(form.is_valid())
        form.send_email()
        return super().form_valid(form)

def success(request):
    return render(request, "shop/success.html")


#방법 1 : 값 고정
# def article_detail(request, id2):
#     # instance = Article.objects.get(id=id2) #앞의 id는 칼럼, 뒤의 id2는 변수
#     instance =get_object_or_404(Article, id=id2)
#     print(instance)
#     return render(request, 'shop/article_detail.html', {'article':instance})

# #방법 2 : 일반화
# def generate_view_func(model):
#     def view_func(request, id2):
#         instance =get_object_or_404(model, id=id2)
#         instance_name = model._meta.model_name
#         print('instance name:', instance_name)
#         print('앱이름:', model._meta.app_label)
        
#         template_name = '{}/{}_detail2.html'.format(model._meta.app_label, instance_name)
#         return render(request, template_name, {instance_name:instance})
#     return view_func

# article_detail = generate_view_func(Article)

#함수 기반
article_detail = DetailView.as_view(model = Article)
#class 기반
class ArticleDV(DetailView):
    model=Article
# artcile_detail = ArticleDV.as_view()


class  MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("MyView의 get 메소드")

from django.views.generic.base import TemplateView
class HomePageView(TemplateView):
    template_name = 'shop/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_list5'] = Article.objects.all()[:5]
        context['mymessage'] = "TGIF!"
        return context

# function 기반 view : (FBV)
# class 기반 view : (CBV)
'''
class DetailView(object): #object를 생략 가능
    def __init__(self, model):
        self.model = model

    def get_object(self, *args, **kwargs):
        return get_object_or_404(self.model, id=kwargs["id2"])

    def get_template_name(self):
        instance_name = self.model._meta.model_name
        template_name = '{}/{}_detail2.html'.format(self.model._meta.app_label, 
                            instance_name)
        return template_name
    def dispath(self, request, *args, **kwargs):
        instance_name = self.model._meta.model_name
        return render(request, self.get_template_name(), 
                        {instance_name:self.get_object(*args, **kwargs)})

# @classmethod 는 클래스에 단 하나 존재함 param도 self 대신 cls를 받는다.
    @classmethod
    def as_view(cls,model):

        def view(request, *args, **kwargs):
            self = cls(model) #모델 생성
            return self.dispath(request, *args, **kwargs)
        return view

article_detail = DetailView.as_view(Article)
'''

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