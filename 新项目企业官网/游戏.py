#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2018/3/30
import pygame
from pygame.locals import *
import time
import random

"""
需求：

设计一个打飞机游戏，实现的功能如下：

1. 能显示我机，可以通过键盘控制飞机位置，按下space键盘可以实现发射子弹  

2. 能自动加载敌机,敌机随机发射子弹，敌机左右移动，每个1秒往下移动。

3. 我机发射的子弹碰到敌机，敌机爆炸，然后消失，我机打中一个记1分，并将得分保存在txt文件中，下次打游戏的时候显示，

默认为零

4. 如果敌机发射的子弹打中我机，Game Over

"""


def main():
    """飞机大战主程序"""
    global window  # 声明成一个全局变量，可以在全部函数使用
    window = pygame.display.set_mode((480, 852), 0, 16)  # 创建一个程序的窗口
    background = Background()
    player = Player()
    hero = HeroPlane()

    enemy_list = []
    enemy = EnemyPlane()
    enemy_list.append(enemy)

    while True:

        ran = random.randint(0, 4)
        if ran == 3:
            for i in range(10):
                enemy = EnemyPlane()
                enemy_list.append(enemy)
        background.display()
        for enemy in enemy_list:
            enemy.autoplay()
        hero.display()
        player.control(hero)
        pygame.display.update()
        check_hit(hero, enemy, enemy_list)
        print(hero.is_alive)
        print(enemy.is_alive)
        time.sleep(0.01)


def check_hit(hero, enemy, enemy_list):
    for bullet in hero.bullets:
        if enemy.x < bullet.x + 11 < enemy.x + 51 and enemy.y < bullet.y + 11 < enemy.y + 39:
            enemy.is_alive = False

    for bullet in enemy.bullets:
        if hero.x < bullet.x + 11 < hero.x + 100 and hero.y < bullet.y + 11 < hero.y + 124:
            hero.is_alive = False
    enemy_dead = []

    for enemy in enemy_list:
        if not enemy.is_alive:
            enemy_dead.append(enemy)
    for enemy in enemy_dead:
        enemy_list.remove(enemy)
    print("{len(enemy_list) } live")


class Image(object):
    """定义一个基类，图片类，
    该图片拥有的属性：
    X---横坐标
    Y---纵坐标
    image_path---图片路径
    image--- pygame 加载图片
    window --- 加载的窗口背景
    """
    count = 0

    def __init__(self, x, y, image_path):
        self.x = x
        self.y = y
        self.image_path = image_path
        self.image = pygame.image.load(image_path)
        self.count += 1

    def display(self):
        window.blit(self.image, (self.x, self.y))


class Background(Image):
    """定义一个背景类，继承图片类的所有属性，作为飞机大战的背景"""

    def __init__(self):
        Image.__init__(self, 0, 0, "./feiji/background.png")


class HeroPlane(Image):
    """
    定义一个飞机类，该飞机拥有图片的所有属性，
    属性：
    is_alive
    bullets
    explode_image
    方法：
    1. 显示自己及自己发射的子弹
    2. 发射子弹，
    3. 管理子弹
    4. 爆炸画面
    5. 可以被控制

    """

    def __init__(self):
        self.x = 240
        self.y = 480
        self.image_path = "./feiji/hero1.png"
        Image.__init__(self, self.x, self.y, self.image_path)
        self.is_alive = True
        self.bullets = []
        self.explode_image_path = "./feiji/hero_blowup_n2.png"

    def display(self):

        if self.is_alive:
            Image.display(self)
        else:
            explode = Image(self.x, self.y, self.explode_image_path)
            explode.display()
        for bullet in self.bullets:
            bullet.display()
            bullet.move_up()
        self.manage_bullets()
        print("我机发射了{len(self.bullets)}颗子弹")

    def manage_bullets(self):
        if len(self.bullets) > 0:
            first_bullet = self.bullets[0]
            if self.bullets[0].y < -22 or self.bullets[0].y > 700:
                self.bullets.remove(first_bullet)

    def shoot(self):
        """发射子弹，主要是创建子弹然后，保存在子弹列表里"""
        bullet = Bullet(self.x + 40, self.y - 18, "./feiji/bullet.png")
        self.bullets.append(bullet)

    def explode(self):
        self.is_alive = False


class EnemyPlane(HeroPlane):
    """创建一个敌机：
    属性：
    bullets[]
    explode_path
    is_alive
    类属性：enemyplane_list

    方法：
    display()
    shoot()
    manage_bullets()
    explode
    move

    """

    def __init__(self):
        self.x = random.randint(50, 430)
        self.y = 50
        self.image_path = "./feiji/enemy0.png"
        Image.__init__(self, self.x, self.y, self.image_path)
        self.explode_image_path = None
        self.is_alive = True
        self.bullets = []
        self.is_direction_right = True
        self.enemy_list = []

    def move(self):
        if self.x > (480 - 50):  # 飞机飞到右边界
            self.is_direction_right = False  # 让飞机往左飞
            self.y += 15
        elif self.x < 0:  # 飞机飞到左边界
            self.is_direction_right = True  # 飞机往右飞
            self.y += 15

        # 根据飞机的方向来设置移动
        if self.is_direction_right:  # 飞机往右飞
            self.x += 5
        else:  # 飞机往左飞
            self.x -= 5

    def autoplay(self):
        if self.is_alive:
            Image.display(self)
            self.move()
            self.shoot()

        for bullet in self.bullets:
            bullet.display()
            bullet.move_down()
        self.manage_bullets()
        print("敌机发射了{len(self.bullets)}颗子弹")
        time.sleep(0.1)

    def shoot(self):
        ran = random.randint(0, 10)
        if ran == 4:
            bullet = Bullet(self.x + 23, self.y + 39, "./feiji/bullet1.png")
            self.bullets.append(bullet)


class Bullet(Image):
    """创建一个子弹类：
    属性：
    image的所有属性
    方法：
    1. 显示
    2. 移动

    """

    def __init__(self, x, y, image_path):
        self.x = x
        self.y = y
        self.image_path = image_path
        Image.__init__(self, self.x, self.y, self.image_path)

    def move_up(self):
        self.y -= 50

    def move_down(self):
        self.y += 30


class Player:
    """创建一个游戏者的类
    游戏者的属性：
    1. 姓名
    2. 得分
    方法：
    1. 控制飞机
    """

    def __init__(self):
        self.name = "hero"
        self.score = 0

    def control(self, plane):
        for event in pygame.event.get():
            # 判断是否是点击了退出按钮
            if event.type == QUIT:
                print("exit")
                exit()
            # 判断是否是按下了键
            elif event.type == KEYDOWN:
                # 检测按键是否是a或者left
                if event.key == K_a or event.key == K_LEFT:
                    print('left')
                    plane.x -= 20
                # 检测按键是否是d或者right
                elif event.key == K_d or event.key == K_RIGHT:
                    plane.x += 20
                    print('right')
                elif event.key == K_w or event.key == K_UP:
                    plane.y -= 20
                    print('right')
                elif event.key == K_s or event.key == K_DOWN:
                    plane.y += 20
                    print('right')
                elif event.key == K_q:
                    plane.explode()
                    print("爆炸")
                # 检测按键是否是空格键
                elif event.key == K_SPACE:
                    plane.shoot()
                    print('space')


if __name__ == '__main__':
    main()

