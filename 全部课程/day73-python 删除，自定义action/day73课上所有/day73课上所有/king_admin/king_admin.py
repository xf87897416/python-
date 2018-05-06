#__author:  Administrator
#date:  2017/1/5
from django.shortcuts import  render,redirect
from crm import models


enabled_admins = {}

class BaseAdmin(object):
    list_display = []
    list_filters = []
    search_fields = []
    list_per_page = 20
    ordering = None
    filter_horizontal = []
    actions = ["delete_selected_objs",]

    def delete_selected_objs(self,request,querysets):
        app_name = self.model._meta.app_label
        table_name = self.model._meta.model_name
        print("--->delete_selected_objs",self,request,querysets)
        if request.POST.get("delete_confirm") == "yes":
            querysets.delete()
            return redirect("/king_admin/%s/%s/" % (app_name,table_name))
        selected_ids =  ','.join([str(i.id) for i in querysets])
        return render(request,"king_admin/table_obj_delete.html",{"objs":querysets,
                                                              "admin_class":self,
                                                              "app_name": app_name,
                                                              "table_name": table_name,
                                                              "selected_ids":selected_ids,
                                                              "action":request._admin_action
                                                              })


class CustomerAdmin(BaseAdmin):
    list_display = ["id",'qq','name','source','consultant','consult_course','date','status']
    list_filters = ['source','consultant','consult_course','status','date','name']
    search_fields = ['qq','name',"consultant__name"]
    filter_horizontal = ('tags',)
    #model = models.Customer
    list_per_page = 5
    ordering = "qq"



    actions = ["delete_selected_objs","test"]
    def test(self,request,querysets):
        print("in test",)
    test.display_name  = "测试动作"

class CustomerFollowUpAdmin(BaseAdmin):
    list_display = ('customer','consultant','date')




class UserProfileAdmin(BaseAdmin):
    list_display = ('user','name')

def register(model_class,admin_class=None):
    if model_class._meta.app_label not in enabled_admins:
        enabled_admins[model_class._meta.app_label] = {} #enabled_admins['crm'] = {}
    #admin_obj = admin_class()
    admin_class.model = model_class #绑定model 对象和admin 类
    enabled_admins[model_class._meta.app_label][model_class._meta.model_name] = admin_class
    #enabled_admins['crm']['customerfollowup'] = CustomerFollowUpAdmin


register(models.Customer,CustomerAdmin)
register(models.CustomerFollowUp,CustomerFollowUpAdmin)
register(models.UserProfile,UserProfileAdmin)



