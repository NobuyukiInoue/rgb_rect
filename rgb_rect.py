# 光の三原色とその組み合わせを３つの四角形の重ね合わせで表現する
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import random
import sys

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
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(u"光の三原色")

    red = colorData()
    green = colorData()
    blue = colorData()

    while True:
        screen.fill((0, 0, 0))

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

if __name__ == "__main__":
    main()
