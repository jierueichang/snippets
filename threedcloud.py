import time, pygame
from random import randint as r
from threed import *
points=[]
for i in range(500):
    points.append([r(-100,100),r(-100,100),r(-100,100)])
'''while True:
    threed.rotateZ(points,0.1)
    threed.rotateY(points,-0.05)
    threed.draw(points)'''
npoints=[
    [-100,-100,100],
    [100,-100,100],
    [100,100,100],
    [-100,100,100],
    [-100,-100,-100],
    [100,-100,-100],
    [100,100,-100],
    [-100,100,-100]
]
px,py=pygame.mouse.get_pos()
while True:
    x,y=pygame.mouse.get_pos()
    screen.fill((0,0,0))
    if 1 in pygame.key.get_pressed():
        speed=3
    else:
        speed=0.00
    rotateX(points,speed)
    rotateY(points,speed)
    rotateZ(points,speed)
    rotateX(npoints,speed)
    rotateY(npoints,speed)
    rotateZ(npoints,speed)
    converge(points)
    if pygame.mouse.get_pressed()[0]:
        if px<x:
            rotateY(points,0.3)
        if px>x:
            rotateY(points,-0.3)
        if py<y:
            rotateX(points,0.3)
        if py>y:
            rotateX(points,-0.3)
        x,y=pygame.mouse.get_pos()

        if px<x:
            rotateY(npoints,0.3)
        if px>x:
            rotateY(npoints,-0.3)
        if py<y:
            rotateX(npoints,0.3)
        if py>y:
            rotateX(npoints,-0.3)
    draw(points,(50,50,50))
    draw(npoints)
    px,py=x,y
    drawnodes(points)
