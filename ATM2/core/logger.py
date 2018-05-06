#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/4


import logging
from conf import settings

def logger(logging_type):

    logger=logging.getLogger(logging_type)
    logger.setLevel(settings.LOGIN_LEVEL)

    ch=logging.StreamHandler()
    ch.setLevel(settings.LOGIN_LEVEL)

    log_file = "%s/log/%s" % (settings.BASE_DIR, settings.LOGIN_TYPE[logging_type])
    fn=logging.FileHandler(log_file)
    fn.setLevel(settings.LOGIN_LEVEL)

    formatter= logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    fn.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger.addHandler(fn)
    logger.addHandler(ch)
    return logger
















