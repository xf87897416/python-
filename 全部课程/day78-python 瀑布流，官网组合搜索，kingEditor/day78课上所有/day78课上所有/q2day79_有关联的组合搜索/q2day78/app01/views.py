from django.shortcuts import render, HttpResponse
from app01 import models


# Create your views here.

def flow(request):
    user_list = [
        {'name': '李二牛', 'src': '/static/image/hero1.png', 'company': '北京其二布莱特科技公司',
         'summary': '公司一群老油条，懒散惯了！对于领导的工作安排也是拖拖拉拉！这样下去不行啊。于是厂长，把他女婿安排进来，监督他们！老油条不愧老油条，没多久。厂长女婿也被他们拖下水，上了他们的贼船……'},
        {'name': '李san牛', 'src': '/static/image/hero1.png', 'company': '技公司', 'summary': '公司一群老'},
        {'name': '李si牛', 'src': '/static/image/hero1.png', 'company': 'sdf公司', 'summary': '拉拉一晚发挥功能'},
        {'name': '李5牛', 'src': '/static/image/hero1.png', 'company': 'sdf公司', 'summary': '拉拉一晚发挥功能'},
        {'name': '李6牛', 'src': '/static/image/1.png', 'company': 'sdf公司', 'summary': '拉拉一晚发挥功能'},
        {'name': '李7牛', 'src': '/static/image/1.png', 'company': 'sdf公司', 'summary': '拉拉一晚发挥功能'},
        {'name': '李8牛', 'src': '/static/image/1.png', 'company': 'sdf公司', 'summary': '拉拉一晚发挥功能'},
    ]
    return render(request, 'flow.html', {'user_list': user_list})


def video1(request, *args, **kwargs):
    # from django.urls import reverse
    #
    # url = reverse('vvv', kwargs={'cg_id': 1, 'lv_id': 2})
    # print(url)

    condition = {}
    for k, v in kwargs.items():
        if v == '0':
            pass
        else:
            condition[k] = v
    direction_list = models.Direction.objects.all()
    category_list = models.Category.objects.all()
    level_list = models.Level.objects.all()

    result = models.Video.objects.filter(**condition)
    return render(request,
                  'video1.html', {
                      'category_list': category_list,
                      'level_list': level_list,
                      'direction_list': direction_list,
                      'result': result,
                      'arg_dict': kwargs
                  })


def video2(request, *args, **kwargs):
    # 0-0-0.html
    # 0-1-0.html
    # 1-0-0.html
    # 1-1-0.html [1,2,3,4]
    # 2-1-0.html [2,3,4]
    dr_id = kwargs.get('dr_id')
    cg_id = kwargs.get('cg_id')
    lv_id = kwargs.get('lv_id')
    condition = {}

    drection_list = models.Direction.objects.all()

    level_list = models.Level.objects.all()

    if dr_id == "0":
        # 未选择方向
        category_list = models.Category.objects.all()
        if cg_id == '0':
            # 未选择分类
            pass
        else:
            # 选择分类
            # models.Video.objects.filter(cg_id=cg_id)
            condition['cg_id'] = cg_id
    else:
        # 选择了方向
        category_list = models.Category.objects.filter(direction=dr_id)

        temp = category_list.values_list('id')
        cg_id_list = list(zip(*temp))[0]

        if cg_id == '0':
            # 未选择分类
            condition['cg_id__in'] = cg_id_list
        else:
            # 选择了分类
            if int(cg_id) in cg_id_list:
                condition['cg_id'] = cg_id
            else:
                condition['cg_id__in'] = cg_id_list
                kwargs['cg_id'] = '0'

    if lv_id == '0':
        pass
    else:
        condition['lv_id'] = lv_id

    result = models.Video.objects.filter(**condition)
    print(result)

    return render(request, 'video2.html', {
        'drection_list': drection_list,
        'level_list': level_list,
        'category_list': category_list,
        'result': result,
        'arg_dict':kwargs
    })
