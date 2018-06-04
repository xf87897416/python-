import time

'''
http://www.cnblogs.com/alex3714/p/6351797.html
学习celery
linux 运行



1 . pip install celery
2. 启动redis
3. 创建celry app
   task.py
    from celery import Celery
    import subprocess,time
    app = Celery('task',
                 broker='redis://:Alex3714@192.168.14.41',
                 backend='redis://:Alex3714@192.168.14.41')
    @app.task
    def add(x, y):
        print("running...", x, y)
        return x + y

    @app.task
    def run_cmd(cmd):
        print('run cmd ...',cmd)
        time.sleep(5)
        cmd_obj = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        return cmd_obj.stdout.read().decode("utf-8")

4. celery -A　task worker --loglevel=info
5. 生成任务
   python3
   >>>:import task
   >>>:r = task.cmd_run.delay("df")
   >>>:r.get()



'''

import celery
































