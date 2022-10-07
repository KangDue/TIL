import socket
from _thread import *
import sys,random

server = ""
port = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    try:
        s.bind((server, port)) #소켓 생성 및 서버 등록,
    except socket.error as e:
        str(e)

    s.listen(6) #최대 플레이어 수
    print("Waiting for a connection, Server Started")


    def threaded_client(conn):
        conn.send(str.encode("Connected"))
        reply = ""
        answer = random.randint(1, 9)
        while True:
            print("정답:",answer)
            try:
                data = conn.recv(2048).decode("utf-8") #읽어오는 함수, 버퍼의 크기 지정
                print(f'데이터:{data}')
                if not data:
                    print("Disconnected")
                    break
                else:
                    print("Received: ", data)
                    print("Sending : ", data)
                # conn.sendall(str.encode(reply))
            except:
                break
            try:
                n = int(data)
            except ValueError:
                conn.sendall(f'입력값이 올바르지 않습니다:{data}'.encode('utf-8'))
                continue
            if n == 0:
                conn.sendall(f"종료".encode('utf-8'))
                break
            if n > answer:
                conn.sendall("너무 높아요".encode('utf-8'))
            elif n < answer:
                conn.sendall("너무 낮아요".encode('utf-8'))
            else:
                conn.sendall("정답".encode('utf-8'))
                break
        conn.sendall(str(players).encode('utf-8'))
        print("Lost connection")
        conn.close()

    players = []
    while True:
        conn, addr = s.accept()
        players.append(conn)
        print("Connected to:", addr)
        for player in players:
            player.sendall("통합했다!".encode('utf-8'))
        start_new_thread(threaded_client, (conn,))