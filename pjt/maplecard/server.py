import socket
from _thread import *
import time
import pygame #파이 게임 모듈 임포트
import random, pygame, sys
from pygame.locals import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "192.168.0.43"
port = 5555


try:
    s.bind((server, port)) #소켓 생성 및 서버 등록,
except socket.error as e:
    str(e)

s.listen(6) #최대 플레이어 수
print("Waiting for a connection, Server Started")

pp = 6
cards = list(range(64))
random.shuffle(cards)
p=[[] for _ in range(pp)]
for i in range(64): #카드 분배
    p[i%pp].append(cards[i])

def getdata(s):
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

def threaded_client(conn):
    global players,ready
    my_id = players.index(conn)
    items = str(p[my_id]).replace(' ','')
    conn.send(str.encode(f"player {my_id} "+items))
    data = False

    while True:
        print(ready)
        if len(players)<=6 and ready: # 준비 완료시
            data = getdata(conn)
            conn.sendall(f'-Now {len(players)} players waiting.-'.encode('utf-8'))
            print(data)
            if data == f'{my_id} ready':
                ready -= 1
                print("하나 완료!")
            continue
        else:
            try:
                data = conn.recv(2048).decode("utf-8") #읽어오는 함수, 버퍼의 크기 지정
                #print(f'데이터:{data}')
                if not data:
                    print("Disconnected")
                    break
                else:
                    print("Received: ", data)
                    print("Sending : ", data)
            except:
                break
            try:
                for co in players:
                    if co == conn: continue
                    if data == "clicked":
                        co.sendall(f"HERE".encode('utf-8'))
                    else:
                        co.sendall("-".encode('utf-8'))
            except ValueError:
                conn.sendall(f'입력값이 올바르지 않습니다:{data}'.encode('utf-8'))
                continue

    players.remove(conn)
    print("Lost connection")
    conn.close()

players = []
ready = 6 # ready한 인원 카운트!
while True:
    conn, addr = s.accept()
    players.append(conn)
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn,))