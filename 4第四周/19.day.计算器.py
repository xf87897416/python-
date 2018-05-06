#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/10/30
import re
def add_sub(a_s):
    if '--' in a_s:
        a_s=a_s.replace('--','+')
    a_s=re.findall('\-?\d+\.?\d*',a_s)
    ls=[]
    for i in range(len(a_s)):
        ls.append(float(a_s[i]))
    return str(sum(ls))
def mu_div(m_d):
    while True:
        m_d01 = re.search(r'[+\-]?\d+\.?\d*[*/][+\-]?(\d+\.?\d*)', m_d)
        if m_d01 == None: return m_d
        if '*' in m_d01.group():
            m_d02=re.findall(r'\d+\.?\d*',m_d01.group())
            result=float(m_d02[0])*float(m_d02[1])
            m_d=re.sub(r'\(?\d+\.?\d*\*(\d+\.?\d*)\)?',str(result),m_d,1)
        elif '/' in m_d01.group():
            m_d03=re.findall(r'\d+\.?\d*',m_d01.group())
            result=float(m_d03[0])/float(m_d03[1])
            m_d = re.sub(r'\(?\d+\.?\d*\/(\d+\.?\d*)\)?',str(result),m_d,1)
        else:break
    return m_d
def result_all(r_a):
    while True:
        if re.findall('[*/]',r_a):
            r_a=mu_div(r_a)
        if re.findall('\d+\.?\d*[+-]',r_a):
            r_a=add_sub(r_a)
        else:break
    return r_a
def remove_breackets(r_b):
    while True:
        if '(' in r_b:
            r_b1=re.search(r'\([^()]+\)',r_b)
            r_b1=result_all(r_b1.group())
            r_b=re.sub(r'\([^()]+\)',str(r_b1),r_b, 1)
        else:break
    return result_all(r_b)
while True:
    run_num="".join(input("请输入表达式：").split())
    print(remove_breackets(run_num.strip()))
# strs='3*(1+9)*2+(1-(2+3))'
# print(eval(strs))










