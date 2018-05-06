#__author:  Administrator
#date:  2017/2/6
from django import template
from django.utils.safestring import mark_safe
register = template.Library()

@register.filter
def test(a1,a2):
    n1,n2 = a2.split(',')
    if a1 % int(n1) == int(n2):
        return True
    return False


@register.simple_tag
def category_tag(obj,arg_dict):
    """
    生成A标签
    :param obj:
    :param arg_dict:
    :return:
    """
    from django.urls import reverse
    url = reverse('vvv', kwargs={'cg_id': obj.id, 'lv_id': arg_dict.get('lv_id')})
    if str(obj.id) == arg_dict.get('cg_id'):
        # 获取当前URL
        tag = "<a class='active' href='%s'>%s</a>" %(url,obj.name)
        return mark_safe(tag)
    else:
        tag = "<a href='%s'>%s</a>" % (url, obj.name)
        return mark_safe(tag)

@register.simple_tag
def level_tag(obj,arg_dict):
    """
    生成A标签
    :param obj:
    :param arg_dict:
    :return:
    """
    from django.urls import reverse
    url = reverse('vvv', kwargs={'cg_id': arg_dict.get('cg_id'), 'lv_id': obj.id})
    if str(obj.id) == arg_dict.get('lv_id'):
        tag = "<a class='active' href='%s'>%s</a>" %(url,obj.name)
        return mark_safe(tag)
    else:
        tag = "<a href='%s'>%s</a>" % (url, obj.name)
        return mark_safe(tag)

@register.simple_tag
def total_tag(arg_dict,key):
    from django.urls import reverse
    if key == 'cg_id':
        url = reverse('vvv', kwargs={'cg_id': 0, 'lv_id': arg_dict.get('lv_id')})
    elif key == 'lv_id':
        url = reverse('vvv', kwargs={'cg_id': arg_dict.get('cg_id'), 'lv_id': 0})
    else:
        url = ""

    tag = "<a href='%s'>全部</a>" % (url,)
    return mark_safe(tag)



###############################################################
@register.simple_tag
def dr_tag(obj,arg_dict):
    """
    生成A标签
    :param obj:
    :param arg_dict:
    :return:
    """

    from django.urls import reverse

    url = reverse('vvv2', kwargs={'dr_id': obj.id, 'cg_id': arg_dict.get('cg_id'), 'lv_id': arg_dict.get('lv_id')})

    if str(obj.id) == arg_dict.get('dr_id'):
        # 获取当前URL
        tag = "<a class='active' href='%s'>%s</a>" %(url,obj.name)
        return mark_safe(tag)
    else:
        tag = "<a href='%s'>%s</a>" % (url, obj.name)
        return mark_safe(tag)


@register.simple_tag
def cg_tag(obj,arg_dict):
    """
    生成A标签
    :param obj:
    :param arg_dict:
    :return:
    """

    from django.urls import reverse

    url = reverse('vvv2', kwargs={'dr_id': arg_dict.get('dr_id'), 'cg_id': obj.id, 'lv_id': arg_dict.get('lv_id')})

    if str(obj.id) == arg_dict.get('cg_id'):
        # 获取当前URL
        tag = "<a class='active' href='%s'>%s</a>" %(url,obj.name)
        return mark_safe(tag)
    else:
        tag = "<a href='%s'>%s</a>" % (url, obj.name)
        return mark_safe(tag)



@register.simple_tag
def lv_tag(obj,arg_dict):
    """
    生成A标签
    :param obj:
    :param arg_dict:
    :return:
    """

    from django.urls import reverse

    url = reverse('vvv2', kwargs={'dr_id': arg_dict.get('dr_id'), 'cg_id': arg_dict.get('cg_id'), 'lv_id': obj.id})

    if str(obj.id) == arg_dict.get('lv_id'):
        # 获取当前URL
        tag = "<a class='active' href='%s'>%s</a>" %(url,obj.name)
        return mark_safe(tag)
    else:
        tag = "<a href='%s'>%s</a>" % (url, obj.name)
        return mark_safe(tag)


@register.simple_tag
def total_tag_2(arg_dict,key):
    from django.urls import reverse
    if key == 'dr_id':
        url = reverse('vvv2', kwargs={'dr_id': 0, 'cg_id': arg_dict.get('cg_id'), 'lv_id': arg_dict.get('lv_id')})
    elif key == 'cg_id':
        url = reverse('vvv2', kwargs={'dr_id': arg_dict.get('dr_id'), 'cg_id': 0, 'lv_id': arg_dict.get('lv_id')})

    elif key == 'lv_id':
        url = reverse('vvv2', kwargs={'dr_id': arg_dict.get('dr_id'), 'cg_id': arg_dict.get('cg_id'), 'lv_id': 0})
    else:
        url = ''
    if arg_dict.get(key) == '0':
        tag = "<a class='active' href='%s'>全部</a>" % (url,)
    else:
        tag = "<a href='%s'>全部</a>" % (url,)
    return mark_safe(tag)
