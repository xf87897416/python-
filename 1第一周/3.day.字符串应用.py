#_author: "Administrator"
#date: 2017/10/22

# a='123'
# b='abc'
# c=a+b
# c="---".join([a,b,c])
# print(c)


#dic={5:'555',2:'666',4:'444'}
# dic.has_keys(5)
# print(5 in dic)
# print(sorted(dic.items()))
# dic5={'name': 'alex', 'age': 18}
#
# for i in dic5:
#     print(i)

# for i,v in dic5.items():
#     print(i,v)


#String 操作

# a="Let's go "
# print(a)
# 1   * 重复输出字符串
# print('hello'*20)

# 2 [] ,[:] 通过索引获取字符串中字符,这里和列表的切片操作是相同的,具体内容见列表
# print('helloworld'[2:])

#关键字 in
# print(123 in [23,45,123])
# print('e2l' in 'hello')

# 4 %   格式字符串
# print('alex is a good teacher')
# print('%s is a good teacher'%'alex')


# String的内置方法

# st='hello kitty {name} is {age}'
#
# print(st.count('l'))       #  统计元素个数
# print(st.capitalize())     #  首字母大写
# print(st.center(50,'#'))   #  居中   一共打印50个字符，其余用'--'
# print(st.endswith('tty3')) #  判断是否以某个内容结尾
# print(st.startswith('he')) #  判断是否以某个内容开头
# print(st.expandtabs(tabsize=20))
# print(st.find('t'))        #  查找到第一个元素，并将索引值返回

# print(st.rfind('t'))    查找最右边的t，返回索引值
# print(st.format(name='alex',age=37))  # 格式化输出的另一种方式   待定：?:{}
# print(st.format_map({'name':'alex','age':22}))
# print(st.index('t'))
# print('asd'.isalnum())
# print('12632178'.isdecimal())
# print('1269999.uuuu'.isnumeric())
# print('abc'.isidentifier())
# print('Abc'.islower())     小写字符
# print('ABC'.isupper())     大写字符
# print('  e'.isspace())     判断空格
# print('My title'.istitle())  每个单词首字母大写才返回true
# print('My tLtle'.lower())    所有大写变小写
# print('My tLtle'.upper())    所有小写变大写
# print('My tLtle'.swapcase()) 大小写反转
# print('My tLtle'.ljust(50,'*'))  向右添加*
# print('My tLtle'.rjust(50,'*'))  向左添加*
# print('\tMy tLtle\n'.strip())
# print('\tMy tLtle\n'.lstrip())
# print('\tMy tLtle\n'.rstrip())
# print('ok')
# print('My title title'.replace('itle','lesson',1))  替换
# print('My title title'.rfind('t'))
# print('My title title'.split('i',1))
# print('My title title'.title())





#摘一些重要的字符串方法
# print(st.count('l'))
# print(st.center(50,'#'))   #  居中
# print(st.startswith('he')) #  判断是否以某个内容开头
# print(st.find('t'))
# print(st.format(name='alex',age=37))  # 格式化输出的另一种方式   待定：?:{}
# print('My tLtle'.lower())
# print('My tLtle'.upper())
# print('\tMy tLtle\n'.strip())
# print('My title title'.replace('itle','lesson',1))
# print('My title title'.split('i',1))
































