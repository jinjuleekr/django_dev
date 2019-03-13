from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book, BookModelForm
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from .forms import BookForm
from django.shortcuts import get_object_or_404


#Ajax에서 403에러를 막는 방법
@csrf_exempt 
def searchData(request):
    data = request.POST['mydata'] #post소문자일 때, 반응하는지 테스트 하기
    #book = Book.objects.get(id = data)
    #print(data)
    # data2 = {'msg' : book.title} : 문자 보내기
    # data2 = {'msg' : book.publication_date.strftime('%Y-%m-%d')} : 날짜(data->string)
    # serialize_book = serialize('json', [book,]) # 객체 보내기
    # serialize_book = serialize_book.strip('[]') #한 건이므로 list 없애기
    
    book = Book.objects.filter(title__contains=data)
    serialize_book = serialize("json", book)
    print(serialize_book)
    # data2 = {'msg' : serialize_book}
    return HttpResponse(json.dumps(serialize_book), 'application/json')
    # return HttpResponse(json.dumps(data2)) # 'application/json'이 default 값으로 넘어간다.

book_list = ListView.as_view(model=Book, paginate_by=10)
book_detail = DetailView.as_view(model=Book)
book_insert = CreateView.as_view(model=Book, fields="__all__")
# book_insert = CreateView.as_view(model=Book, fields=[])
book_update = UpdateView.as_view(model=Book, fields="__all__")
book_delete = DeleteView.as_view(model=Book, success_url="/book/")

def book_update(request, pk):
    book = get_object_or_404(Book, id=pk)
    if request.method == 'POST':
        form = BookModelForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.ip = '.'.join(request.META['REMOTE_ADDR'].split('.')[:-1]) + ".88"
            book.save()
            return redirect('/book/')
    else:
        form = BookModelForm(instance=book)
    return render(request, 'book/book_form.html', {'form':form})


def book_insert(request):
    if request.method=='GET':
        # form = BookForm()
        form = BookModelForm()
    else:
        print('저장한다.')
        # form = BookForm(request.POST, request.FILES)
        form = BookModelForm(request.POST, request.FILES)
        if form.is_valid():
            
            #ModelForm ... commit 지연
            book = form.save(commit=False)
            book.ip = request.META['REMOTE_ADDR']
            book.save()
            return redirect(reverse('book:list'))
            
            # Book.objects.create(**form.cleaned_data)
            # return redirect(reverse('book:list'))

            # .cleaned_data 유효성 검사가 끝난 데이터, dic형태로 return
            ######### 방법3 ##############
            # Book.objects.create(title = form.cleaned_data['title'],
            #                     author = form.cleaned_data['author'],
            #                     publisher = form.cleaned_data['publisher'])
            # return redirect(reverse('book:list'))

            ######### 방법2 ##############
            # book = Book(title = form.cleaned_data['title'],
            #             author = form.cleaned_data['author'],
            #             publisher = form.cleaned_data['publisher'])
            # book.save()
            # return redirect(reverse('book:list'))

            ######### 방법1 ###########
            # book = Book()
            # book.title = form.cleaned_data['title']
            # book.author = form.cleaned_data['author']
            # book.publisher = form.cleaned_data['publisher']
            # book.save()
            # return redirect(reverse('book:list'))

            '''
            print("request.POST: ", request.POST)
            print(form)
            print(form.cleaned_data) #{}
            form.save()
            # return redirect("/book/")
            return redirect(reverse('book:list'))
            '''

    return render(request, 'book/book_form.html', {'form': form})

# index = ListView.as_view(model=Outsourcing, paginate_by=10, template_name='kmong/list.html')

class BookListView(ListView):
    model=Book
    paginate_by=5
    template_name='book/book_list.html'

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5  # Display only 5 page numbers
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range
        return context

book_list = BookListView.as_view()