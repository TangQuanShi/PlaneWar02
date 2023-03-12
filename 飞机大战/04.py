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
while True:
    pass

pygame.quit()