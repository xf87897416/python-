#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2018/5/22

import time
'''
学习git
http://www.cnblogs.com/alex3714/articles/5930846.html


配置用户名：git config --global user.name "你的用户名"

配置邮箱 ：git config --global user.email "你的邮箱"

删除错误配置 ：git config --global --unset "错误的key删除掉"

查看配置 ：git config --list

查看文件区别   git diff first.txt  

查看日志  git log
         git reflog 查看所有日志
         git log --pretty=oneline  只查看一行

版本回退
命令:git reset --hard HEAD^
回到最近一次提交的版本的文件状态

git reset --hard 8fbe7e9c42efba7b6c5b4


命令: git add ./file.txt
    将当前目录中的file.txt添加到暂存区
    或者: git add .

git checkout -- file.txt 将文件恢复（前提是没有add）
git reset file.txt 将文件恢复到暂存区，然后执行上面（已经add，但没有commit）


将文件添加到仓储中
    命令 : git commit -m "这次我添加了一个变量"

----------------------------------------------------
通过SSH登录，不用在输入用户名和密码
    1.在任意位置输入 ssh-keygen -t rsa 创建rsa密钥
    将公钥输入到github上面


    git remote add origin git@github.com:xf87897416/git_learn.git
    连接远程仓库
     git push -u origin master 本地代码推送上去

    pull（拉回)
    命令：git pull [地址] master
    或命令：git pull origin master


 新的机器 git clone https://github.com/xf87897416/git_learn.git
 这样就克隆了
 -------------------------------------------------------

查看有多少分支
    git branch

命令: git branch dev
    创建了一个名为dev的分支

命令: git checkout dev
    切换到dev分支

创建并切换到指定分支
    git checkout -b dev



命令: git merge dev
    表示将当前分支与dev分支合并

在主分支下执行合并命令.
    命令: git branch -d dev
    表示删除dev分支,当合并分支后，如果不需要再使用dev分支，则可以直接删除。
    不要在dev分支执行这个命令，在别的的分支执行


stash相关常用命令：
    用于开发一半但未提交，然后保存现有修改
git stash             将当前工作区所有修改过的内容存储到“某个地方”，将工作区还原到当前版本未修改过的状态
git stash list        查看“某个地方”存储的所有记录
git stash clear     清空“某个地方”
git stash pop       将第一个记录从“某个地方”重新拿到工作区（可能有冲突）
git stash apply     编号, 将指定编号记录从“某个地方”重新拿到工作区（可能有冲突） 
git stash drop      编号，删除指定编号的记录


pul request  先fork 然后本地clone 创建分支，push上  添加pull request




'''
























