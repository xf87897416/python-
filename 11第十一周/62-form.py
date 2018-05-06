#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/12/26

import time
import datetime
'''


用户提交数据的验证：
1创建模板                    class LoginForm（forms.Form）
2将请求交给模板，创建一个对象  obj=LoginForm(request.POST)
3进行验证                    obj.is_valid（）
4获取正确信息                obj.clean()
5获取错误信息                obj.errors()



用法：
    user1 = fields.CharField()
    user2 = fields.CharField(widget=widgets.TextInput)
    user3 = fields.CharField(widget=widgets.TextInput(attrs={}))
    特殊的：
        单值：
        user4 = fields.CharField(widget=widgets.Select(attrs={},choices=[(),(),()]))
        user4 = fields.ChoiceField(choices=[(),(),()],widget=widgets.Select)
        
        
        
        # 多值
        user4 = fields.CharField(widget=widgets.MutipleSelect(attrs={},choices=[(),(),()]))
        # "[1,2,3]"
        user4 = fields.MultipleChoiceField(widget=widgets.MutipleSelect(attrs={},choices=[(),(),()]))
        # [1,2,3,4]






'''

# current_date = datetime.datetime.now()
# print(current_date)
# limit_day = current_date - datetime.timedelta(hours=1)
# print(limit_day)
_letter_cases = "abcdefghjkmnpqrstuvwxy"  # 小写字母，去除可能干扰的i，l，o，z
_upper_cases = _letter_cases.upper()  # 大写字母
_numbers = ''.join(map(str, range(3, 10)))  # 数字

init_chars = ''.join((_letter_cases, _upper_cases, _numbers))
print(init_chars)



