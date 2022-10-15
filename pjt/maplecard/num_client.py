import socket
import random, pygame, sys

HOST = '192.168.0.43'
PORT = 5555

pygame.init() #파이 게임 초기화
swidth,sheight= 1000, 800
screen = pygame.display.set_mode((swidth, sheight)) #화면 크기 설정
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

background = pygame.display.set_mode((swidth,sheight))
pygame.display.set_caption("text")

# 글자체(text font) 지정하기
myFont = pygame.font.SysFont(None, 50)  # (글자체, 글자크기) None=기본글자체

# 변수
x_pos = 0
y_pos = 0

play = True
flag = False

def getdata():
    data = s.recv(2048).decode('utf-8')
    try:
        data = data.split('-')
        for i in data:
            if i:
                data = i
                break
        return data
    except:
        return '-'


people = 0
ready = pygame.image.load(f"images/bready.png")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = ''
    my_cards = []
    stored = []
    turn = False
    my_id = -1
    while play:
        screen.fill(WHITE)  # 단색으로 채워 화면 지우기
        width_each = min((swidth - 50) // len(my_cards), 250) if my_cards else 10
        height_each = min(width_each * 2, 270)
        # 변수 업데이트
        event = pygame.event.poll()  # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
            elif event.type == pygame.MOUSEBUTTONDOWN and turn:
                s.sendall(f'{my_id} clicked'.encode('utf-8'))
            elif event.type == pygame.MOUSEBUTTONDOWN and x_pos >= 900 and y_pos <=100 and my_id >-1: #준비하기.
                ready = pygame.image.load(f"images/aready.png")
                s.sendall(f'-{my_id} ready-'.encode('utf-8'))
            elif event.type == pygame.MOUSEBUTTONDOWN:
                column_index = event.pos[0] // width_each
                row_index = event.pos[1] // height_each
                if my_cards:
                    stored.append(my_cards.pop(column_index))
                print(column_index, row_index)
        # end of for
        background.fill((255, 255, 0))  # 배경 노란색
        x_pos, y_pos = pygame.mouse.get_pos()  # 마우스 x,y좌표값 저장
        # render함수로 글자출력(문자열이 아니면 str로 변환해야함)
        myText = myFont.render("Hello World " + str(x_pos), True, (0, 0, 255))  # (Text,anti-alias, color)
        background.blit(myText, (10, 100))  # (글자변수, 위치)
        #s.sendall(f'{x_pos}{y_pos}'.encode('utf-8'))
        s.sendall('-'.encode('utf-8'))
        data = getdata()
        if type(data)==list: #error 처리
            data = '-'

        myText2 = myFont.render(data, True, (0, 0, 255))  # (Text,anti-alias, color)
        background.blit(myText2, (200, 200))  # (글자변수, 위치)
        print(my_id)
        #id, 카드 받아오기
        if len(data) >= 8 and data[:6]=='player':
            data = data.split()
            my_id = int(data[1])
            my_cards = eval(data[2])

        #인원 수 상단 표기
        if len(data)>16 and data[-16:]=="players waiting." and data[4].isdigit():
            people = int(data[4])
        people_now = myFont.render(f'Now {people}/6', True, (0, 0, 255))
        background.blit(people_now, (10, 10))  # (글자변수, 위치)

        #준비 버튼
        ready_state = pygame.transform.scale(ready, (100, 50))
        screen.blit(ready_state, pygame.Rect(900, 0, 1000, 50))

        card_img = []
        for i in range(len(my_cards)):
            card = pygame.image.load(f"images/{my_cards[i]}.jfif")
            card = pygame.transform.scale(card, (width_each - 2.5, height_each - 2.5))
            card_img.append(card)

        for cw in range(len(my_cards)):
            pygame.draw.rect(screen, BLACK, pygame.Rect(width_each * cw, 100, width_each, height_each), 1)
            screen.blit(card_img[cw], pygame.Rect(width_each * cw, 100, width_each, height_each))

        s_width_each = min((swidth - 50) // len(stored), 250) if stored else 10
        s_height_each = min(s_width_each * 2, 270)
        for i in range(len(stored)):
            card = pygame.image.load(f"images/{stored[i]}.jfif")
            card = pygame.transform.scale(card, (s_width_each - 2.5, s_height_each - 2.5))
            screen.blit(card, pygame.Rect(s_width_each * i, 500, s_width_each, 500 + s_height_each))



        pygame.display.update()
        pygame.time.wait(100)

    pygame.quit()
