import pygame #파이 게임 모듈 임포트
import random, pygame, sys
from pygame.locals import *

player = 6
cards = list(range(64))
random.shuffle(cards)
p=[[] for _ in range(player)]
for i in range(64): #카드 분배
    p[i%player].append(cards[i])


my_cards = p[random.randint(0,player-1)]
pygame.init() #파이 게임 초기화
swidth,sheight= 1000, 800
screen = pygame.display.set_mode((swidth, sheight)) #화면 크기 설정
clock = pygame.time.Clock()
"""
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
YELLOW = (255, 255, 0)
"""
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

stored=[]
#변수
while True: #게임 루프
    screen.fill(BLACK) #단색으로 채워 화면 지우기
    width_each = min((swidth - 50) // len(my_cards),250) if my_cards else 1
    height_each = min(width_each * 2,270)
    #변수 업데이트
    event = pygame.event.poll() #이벤트 처리
    if event.type == pygame.QUIT:
        break
    elif event.type == pygame.MOUSEBUTTONDOWN:
        column_index = event.pos[0] // width_each
        row_index = event.pos[1] // height_each
        if my_cards:
            stored.append(my_cards.pop(column_index))
        print(column_index, row_index)

    card_img = []
    for i in range(len(my_cards)):
        card = pygame.image.load(f"images/{my_cards[i]}.jfif")
        card = pygame.transform.scale(card, (width_each-2.5, height_each-2.5))
        card_img.append(card)

    for cw in range(len(my_cards)):
        print(width_each, height_each)
        pygame.draw.rect(screen, BLACK, pygame.Rect(width_each*cw, 100, width_each, height_each), 1)
        screen.blit(card_img[cw], pygame.Rect(width_each*cw, 100, width_each, height_each))

    s_width_each = min((swidth - 50) // len(stored),250) if stored else 1
    s_height_each = min(s_width_each * 2,270)
    for i in range(len(stored)):
        card = pygame.image.load(f"images/{stored[i]}.jfif")
        card = pygame.transform.scale(card, (s_width_each-2.5, s_height_each-2.5))
        screen.blit(card, pygame.Rect(s_width_each * i, 500, s_width_each, 500+s_height_each))

    ###
    pygame.display.update() #모든 화면 그리기 업데이트
    clock.tick(30) #30 FPS (초당 프레임 수) 를 위한 딜레이 추가, 딜레이 시간이 아닌 목표로 하는 FPS 값

pygame.quit()