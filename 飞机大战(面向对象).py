import random

import pygame
from pygame import *
import time

class HeroPlane(object):
    def __init__(self,screen):

        # 创建一个图片，玩家飞机
        self.player = pygame.image.load("./飞机大战图片素材/hero1.png")
        # 定义飞机坐标
        self.x = 480/2-100/2
        self.y = 600
        # 飞机速度
        self.speed = 10
        # 记录当前的窗口对象
        self.screen = screen
        #装子弹的列表
        self.bullets=[]
    def key_control(self):
        # 监听键盘事件
        key_pressed = pygame.key.get_pressed()

        if key_pressed[K_w] or key.get_pressed()[K_UP]:
            self.y -= self.speed
        if key_pressed[K_s] or key.get_pressed()[K_DOWN]:
            self.y += self.speed
        if key_pressed[K_a] or key.get_pressed()[K_LEFT]:
            self.x -= self.speed
        if key_pressed[K_d] or key.get_pressed()[K_RIGHT]:
            self.x += self.speed
        if key_pressed[K_SPACE]:
            #按下空格发射子弹
            bullet=Bullet(self.screen,self.x,self.y)
            #把子弹放到列表里
            self.bullets.append(bullet)
    def display(self):
        # 将飞机图片贴到窗口中
        self.screen.blit(self.player, (self.x, self.y))
        #遍历所有子弹
        for bullet in self.bullets:
            #让子弹飞 修改子弹y坐标
            bullet.auto_more()
            #子弹显示在窗口
            bullet.display()
class EnemyPlane(object):
    def __init__(self,screen):

        # 创建一个图片，敌方飞机
        self.player = pygame.image.load("./飞机大战图片素材/enemy1.png")#57*51
        # 定义飞机坐标
        self.x = 0
        self.y = 0
        # 飞机速度
        self.speed = 10
        # 记录当前的窗口对象
        self.screen = screen
        #装子弹的列表
        self.bullets=[]
        #敌机移动的方向
        self.direction='right'

    def display(self):
        # 将飞机图片贴到窗口中
        self.screen.blit(self.player, (self.x, self.y))
        #遍历所有子弹
        for bullet in self.bullets:
            #让子弹飞 修改子弹y坐标
            bullet.auto_more()
            #子弹显示在窗口
            bullet.display()
    def auto_move(self):
        if self.direction=='right':
            self.x+=self.speed
        elif self.direction=='left':
            self.x -= self.speed
        if self.x>480-57:#屏幕-飞机宽度
            self.direction='left'
        elif self.x<0:
            self.direction='right'
    def auto_fire(self):
        """自动开火 创建子弹对象 添加进列表"""
        random_num=random.randint(1,20)
        if random_num==8:
            bullet=EnemyBullet(self.screen,self.x,self.y)
            self.bullets.append(bullet)
#子弹类
#属性
class Bullet(object):
    def __init__(self,screen,x,y):
        #坐标
        self.x=x+100/2-10/2
        self.y=y-22
        #图片
        self.image=pygame.image.load("./飞机大战图片素材/bullet2.png")
        #窗口
        self.screen = screen
        #速度
        self.speed=10
    def display(self):
        """显示子弹到窗口"""
        self.screen.blit(self.image,(self.x,self.y))
    def auto_more(self):
        """让子弹飞 修改子弹y坐标"""
        self.y-=self.speed
#敌方子弹类
#属性
class EnemyBullet(object):
    def __init__(self,screen,x,y):
        #坐标
        self.x=x+56/2-8/2
        self.y=y+39
        #图片
        self.image=pygame.image.load("./飞机大战图片素材/bullet1.png")
        #窗口
        self.screen = screen
        #速度
        self.speed=10
    def display(self):
        """显示子弹到窗口"""
        self.screen.blit(self.image,(self.x,self.y))
    def auto_more(self):
        """让子弹飞 修改子弹y坐标"""
        self.y+=self.speed

class GameSound(object):
    pygame.mixer.init()  #音乐模块初始化
    pygame.mixer.music.load("./sound/game_music.ogg")
    pygame.mixer.music.set_volume(0.5)   #声音大小
    def playBackgroundMusic(self):
        pygame.mixer.music.play(-1)  #开始播放音乐(-1)表示循环播放，写数字几就放几遍


def main():
    """完成整个程序的控制"""
    sound=GameSound()
    sound.playBackgroundMusic()
    #创建一个窗口
    screen=pygame.display.set_mode((480,852),0,32)
    #创建一个图片，当作背景
    background=pygame.image.load("./飞机大战图片素材/background.png")
    #创建一个飞机的对象，注意不要忘记传窗口
    player=HeroPlane(screen)
    # 创建一个敌方飞机的对象，注意不要忘记传窗口
    enenmyplane = EnemyPlane(screen)

    while True:
        # 将背景图片贴到窗口中
        screen.blit(background, (0, 0))

        #获取事件
        for event in pygame.event.get():
            #判断事件类型
            if event.type == QUIT:
                #执行pygame退出
                pygame.quit()
                #python程序退出
                exit()
        #执行飞机的按键监听
        player.key_control()
        #飞机的显示
        player.display()
        #敌方飞机的显示
        enenmyplane.display()
        #敌机自动移动
        enenmyplane.auto_move()
        # 敌机自动开火
        enenmyplane.auto_fire()
        #显示窗口中的内容
        pygame.display.update()
        time.sleep(0.01)
if __name__=="__main__":
    main()
