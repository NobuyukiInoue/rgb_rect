# 光の三原色とその組み合わせを３つの四角形の重ね合わせで表現する
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import random
import sys
from time import sleep

class colorData:
    """各三原色の明るさを管理するクラス"""
    def __init__(self):
        """インスタンス初期化"""
        self.color = 0
        self.step = random.randint(2, 4)

    def nextColor(self):
        """次に描画する明るさをセットする"""
        self.color += self.step
        if self.color > 255:
            self.color = 255
            self.step = -random.randint(2, 4)
        elif self.color < 0:
            self.color = 0
            self.step = random.randint(2, 4)

    def Color(self):
        """現在の明るさを返す"""
        return self.color

def main():
    """メイン"""
    pygame.init()
    SCREEN_SIZE = (640, 480)
    screen1 = pygame.display.set_mode(SCREEN_SIZE)
    screen2 = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(u"光の三原色")

    red = colorData()
    green = colorData()
    blue = colorData()

    while True:
        screen1.fill((0, 0, 0))
        #screen2.fill((255, 255, 255))

        draw_posi(screen1, red, green, blue)
        #draw_nega(screen2, red, green, blue)

        sleep(0.01)
        # 次に描画する明るさをセットする
        red.nextColor()
        green.nextColor()
        blue.nextColor()

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(1)
        #break

def draw_posi(screen, red, green, blue):
    # Red
    pygame.draw.rect(screen, (red.Color(), 0, 0), Rect(200, 100, 200, 100))
    # Green
    pygame.draw.rect(screen, (0, green.Color(), 0), Rect(133, 200, 67, 200))
    # Blue
    pygame.draw.rect(screen, (0, 0, blue.Color()), Rect(400, 200, 67, 200))                
    # Yellow
    pygame.draw.rect(screen, (red.Color(), green.Color(), 0), Rect(200, 200, 67, 100))
    # White
    pygame.draw.rect(screen, (red.Color(), green.Color(), blue.Color()), Rect(267, 200, 67, 100))
    # Magenta
    pygame.draw.rect(screen, (red.Color(), 0, blue.Color()), Rect(333, 200, 67, 100))
    # Green
    pygame.draw.rect(screen, (0, green.Color(), 0), Rect(200, 300, 100, 100))
    # Sky
    pygame.draw.rect(screen, (0, green.Color(), blue.Color()), Rect(267, 300, 67, 100))
    # Blue
    pygame.draw.rect(screen, (0, 0, blue.Color()), Rect(333, 300, 67, 100))

def draw_nega(screen, red, green, blue):
    # Red
    pygame.draw.rect(screen, (255 - red.Color(), 255, 255), Rect(200, 100, 200, 100))
    # Green
    pygame.draw.rect(screen, (255, 255 - green.Color(), 255), Rect(133, 200, 67, 200))
    # Blue
    pygame.draw.rect(screen, (255, 255, blue.Color()), Rect(400, 200, 67, 200))                
    # Yellow
    pygame.draw.rect(screen, (255 - red.Color(), 255 - green.Color(), 255), Rect(200, 200, 67, 100))
    # White
    pygame.draw.rect(screen, (255 - red.Color(), 255 - green.Color(), 255 - blue.Color()), Rect(267, 200, 67, 100))
    # Magenta
    pygame.draw.rect(screen, (255 - red.Color(), 255, 255 - blue.Color()), Rect(333, 200, 67, 100))
    # Green
    pygame.draw.rect(screen, (255, 255 - green.Color(), 255), Rect(200, 300, 100, 100))
    # Sky
    pygame.draw.rect(screen, (255, 255 - green.Color(), 255 - blue.Color()), Rect(267, 300, 67, 100))
    # Blue
    pygame.draw.rect(screen, (255, 255, 255 - blue.Color()), Rect(333, 300, 67, 100))

if __name__ == "__main__":
    main()
