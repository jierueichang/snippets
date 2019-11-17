import pygame
from pygame.locals import *
from math import cos,sin
pygame.init()

pygame.display.set_caption('Threed')

screenx=600
screeny=400
screen=pygame.display.set_mode((600,400))

fpsclock=pygame.time.Clock()

def parallax(points):
    return points
    newpoints = []
    for point in points:
        pxAmountX = point[2]*0.10
        pxAmountY = point[2]*0.10
        if point[0]<0:
            npoint0 = point[0]+pxAmountX
        else:
            npoint0 = point[0]-pxAmountX
        if point[1]<0:
            npoint1 = point[1]+pxAmountY
        else:
            npoint1 = point[1]-pxAmountY
        newpoints.append([npoint0,npoint1,point[2]])
    return newpoints

def rotateZ(points,radians):
    c=cos(radians)
    s=sin(radians)
    for i in points:
        x=i[0]
        y=i[1]
        i[0]=x*c-y*s
        i[1]=y*c+x*s

def rotateY(points,radians):
    c=cos(radians)
    s=sin(radians)
    for i in points:
        x=i[0]
        z=i[2]
        i[0]=x*c-z*s
        i[2]=z*c+x*s

def rotateX(points,radians):
    c=cos(radians)
    s=sin(radians)
    for i in points:
        z=i[2]
        y=i[1]
        i[1]=y*c-z*s
        i[2]=z*c+y*s

def clearscreen():
    screen.fill((0,0,0))

def draw(points,color=(255,255,255),offset=[0,0]):
    global screenx, screeny,fpsclock
    cpoints=[]
    npoints = parallax(points)
    for i in npoints:
        cpoints.append([i[0]+screenx/2+offset[0],i[1]+screeny/2+offset[1]])
    pygame.draw.aalines(screen,color,True,cpoints,5)
    pygame.display.flip()

def drawnodes(points):
    global screenx, screeny, fpsclock, screen
    for i in points:
        try:
            pygame.draw.circle(screen,(200,250,200),(int(round(i[0]+screenx/2)),int(round(i[1]+screeny/2))),3)
        except:
            #print(i)
            del i
    pygame.display.flip()
    for i in pygame.event.get():
        if i.type==QUIT:
            pygame.quit()
    fpsclock.tick(10)

def converge(points):
    for i in points:
        if i[0]+i[1]+i[2]>1000:
            i[0]/=100
            i[1]/=100
            i[2]/=100
        else:
            i[0]/=0.91
            i[1]/=0.91
            i[2]/=0.91

def main():
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
        if px<x:
            rotateY(npoints,0.1)
        if px>x:
            rotateY(npoints,-0.1)
        if py>y:
            rotateX(npoints,0.1)
        if py<y:
            rotateX(npoints,-0.1)
        draw(npoints)
        px,py=x,y

if __name__=='__main__':
    main()
