#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/11

import os,sys

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,BASE_DIR)

from core import main
from conf import settings



if __name__ == '__main__':
    obj = main.Manage_center()
    obj.run()



















