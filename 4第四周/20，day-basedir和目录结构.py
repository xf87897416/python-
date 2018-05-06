#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/1

import sys
import os

# print(sys.path)
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

print(sys.path)
print(__name__)

if __name__ =='__main__':
    print('ok')





















