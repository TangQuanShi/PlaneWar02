import pygame
hero_rect = pygame.Rect(100,500,120,125)
print("英雄的原点 %d %d" %(hero_rect.x,hero_rect.y))
print("英雄的尺寸 %d %d" %(hero_rect.width,hero_rect.y))
print("%d %d" % hero_rect.size)#矩形的宽度，高度