import pygame
from network import Network

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0

from collections import Counter
class Player():
    def __init__(self, own_cards, play_num, own_stored=[]):
        self.own_cards = own_cards
        self.play_num = play_num
        self.own_stored = own_stored

    def lose(self, lose):
        pygame.draw.rect(lose, self.color, self.rect)

    def give(self,other):
        self.give = int(input())


    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)


def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

def main():
    run = True
    n = Network()
    my_card = read_card(n.getcard())
    p = Player(my_card,clientNumber)
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2Pos = read_pos(n.send())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        pygame.display.update()

main()