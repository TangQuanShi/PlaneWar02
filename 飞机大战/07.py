import pygame
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
screen.blit(hero,(200,500))
pygame.display.update()
#创建时钟对象
clock = pygame.time.Clock()
#游戏循环意味着游戏的正式开始
i=0

while True:
    #可以指定循环体内部的代码执行的频率
    clock.tick(1)
    i+=1
    print(i)
    pass

pygame.quit()