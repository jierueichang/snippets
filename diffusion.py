import pygame
from random import randint
from pygame.locals import *
pygame.init()

pygame.display.set_caption('Diffusion Simulator')
screen = pygame.display.set_mode((800,400))
particles = []

displayFont = pygame.font.SysFont('Inconsolata',40)

temp = 1
coolspeed = 0.0001

for i in range(50):
    particles.append([randint(0,400),randint(0,400),randint(-temp,temp),randint(-temp,temp),(200,255,200)]) # initialx, initialy, xvel, yvel
for i in range(1000):
    particles.append([randint(400,800),randint(0,400),randint(-temp,temp),randint(-temp,temp),(200,200,255)])

def move(particle, coolspeed):
    if particle[0] > 800 or particle[0] < 0:
        particle[2] *= -1
    if particle[1] > 400 or particle[1] < 0:
        particle[3] *= -1
    particle[0] += int(round(particle[2]))
    particle[1] += int(round(particle[3]))
    particle[2] *= 1-coolspeed
    particle[3] *= 1-coolspeed

def count(particles):
    bound = 400
    l = 0
    r = 0
    for i in particles:
        if i[0] < bound:
            l += 1
        else:
            r += 1
    return l,r

def main(particles):
    frameClock = pygame.time.Clock()
    while True:
        screen.fill((0,0,0))
        pygame.draw.line(screen, (255,200,200), (400,0) ,(400,400), 2)
        l,r=count(particles)

        for i in particles:
            move(i, coolspeed)
            pygame.draw.circle(screen, i[-1], (i[0], i[1]), 5)

        screen.blit(displayFont.render(str(l), 1, (255,200,200)), (10,10))
        screen.blit(displayFont.render(str(r), 1, (255,200,200)), (760,10))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
        frameClock.tick(40)
        pygame.display.flip()

if __name__ == '__main__':
    main(particles)
