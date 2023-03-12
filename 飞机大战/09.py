import pygame
from plane_sprites import *
pygame.init()
screen=pygame.display.set_mode((480,700))#窗口
# 绘制背景图像
# 1.加载图像数据
bg = pygame.image.load("D:/飞机大战/images/background.png")
# 2.bilt绘制图像
screen.blit(bg, (0,0))
# 3.update更新图像显示
pygame.display.update()

#绘制英雄飞机
hero=pygame.image.load("D:/飞机大战/images/me1.png")
screen.blit(hero,(150,300))
pygame.display.update()
#创建时钟对象
clock = pygame.time.Clock()
#游戏循环意味着游戏的正式开始

#1.定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150,300,102,126)


#创建敌机精灵
enemy1 = GameSprite("D:/飞机大战/images/enemy1.png")
enemy2= GameSprite("D:/飞机大战/images/enemy1.png",2)
#创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy1,enemy2)


while True:
    #可以指定循环体内部的代码执行的频率
    clock.tick(60)
    #监听事件(非常固定的代码)
    for event in pygame.event.get():
        #判断事件类型是否是退出事件
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #2，修改飞机的位置
    hero_rect.y -=1
    #移出屏幕就重新飞出
    if hero_rect.y<=0:
        hero_rect.y=700
    #3.调用blit方法绘制图像
    screen.blit(bg,(0,0))
    screen.blit(hero,hero_rect)

    #让精灵组调用两个方法
    #update--让组中的所有精灵更新位置
    enemy_group.update()
    #draw--绘制所有精灵
    enemy_group.draw(screen)
    #4.调用update方法更新显示
    pygame.display.update()
    pass

pygame.quit()