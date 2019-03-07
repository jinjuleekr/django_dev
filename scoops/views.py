from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello Django Project. Responsing...")

def test1(request):
    return HttpResponse("test1메서드로 응답합니다.")

def test2(request):
    return HttpResponse("test2메서드로 응답합니다.")
    
def test3(request, year):
    return HttpResponse("test3메서드로 응답합니다.{}".format(year))    

def test4(request, year):
    return HttpResponse("test4메서드로 응답합니다.{}".format(year))    

def test5(request, year):
    print(year)
    return HttpResponse("test5메서드로 응답합니다.{}".format(year))

def test6(request, year, month):
    print(year, month)
    return HttpResponse("test6메서드로 응답합니다.{}년도 {}월".format(year, month))

def test7(request, alphabet):
    print(alphabet)
    return HttpResponse("test5메서드로 응답합니다.{}".format(alphabet))

def test8(request, alphabet, alphabet2):
    print(alphabet, alphabet2)
    return HttpResponse("test5메서드로 응답합니다.{}-{}".format(alphabet, alphabet2))

def func1(request, year, month, myname):
    print( year, month, myname)
    return HttpResponse("func메서드로 응답합니다.{}연도 {}월 {}".format(year, month, myname))

def func2(request, num):
    print(num)
    return HttpResponse("func2메서드로 응답합니다.{}".format(num))