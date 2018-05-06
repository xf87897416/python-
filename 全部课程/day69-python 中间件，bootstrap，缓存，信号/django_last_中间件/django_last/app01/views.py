from django.shortcuts import render,HttpResponse

# Create your views here.

class Foo:
    def __init__(self, request,html):
        self.req = request
        self.html = html


    def render(self):
        return render(self.req,self.html)


def test(request,nid):
    print('views')
    # int('asdf')
    # return HttpResponse('TEST')
    # return render(request, 'test.html')
    # --> HttpResponse
    return Foo(request,'test.html')



def index(request):
    print(request.method)
    # return Foo(request,'index.html')
    return render(request,'index.html')

from django.views.decorators.cache import cache_page

@cache_page(10)
def part(request):
    import time
    v=time.time()
    return render(request,'part.html',{'v':v})






