from django.shortcuts import render,HttpResponse
from  app01 import tasks
# Create your views here.
from celery.result import AsyncResult

import time

def index(request):

    res = tasks.add.delay(5,999)

    print("res:",res)
    return HttpResponse(res.task_id)


def task_res(request):

    result = AsyncResult(id="8759c00e-8d22-4e80-a65d-20d999bce200")

    #return HttpResponse(result.get())
    return HttpResponse(result.status)