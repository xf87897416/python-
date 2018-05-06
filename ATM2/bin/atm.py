#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/3

import os,sys

dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir)
print(sys.path)

from core import main

if __name__ == '__main__':
    main.run()



















