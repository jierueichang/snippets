import threed, random, pygame
from pygame.locals import *

def tree(x,z,w,l,scale=1):
    coords = [
        [0,0,0],
        [0,0,50],
        [50,0,50],
        [50,0,0],
        [0,0,0],
        [25,0,25],
        [25,30,25],
        [15,40,15],
        [25,50,25],
        [35,40,35],
        [25,30,25],
        [15,40,35],
        [25,50,25],
        [35,40,15],
        [25,30,25],
        [25,0,25]
    ]
    for i in coords:
        for j in range(len(i)):
            i[j] = i[j]*scale
        #print i
        i[0]+=(x-w)
        i[2]+=(z-l)
        i[1]*=-1
    #print coords
    return coords

def house(x,z,w,l,scale=1):
    coords = [
        [0,0,0],
        [0,0,50],
        [50,0,50],
        [50,0,0],
        [0,0,0],
        [10,0,10],
        [10,15,10],
        [25,20,10],
        [25,20,40],
        [40,15,40],
        [40,0,40],
        [40,0,10],
        [40,15,10],
        [25,20,10],
        [25,20,40],
        [10,15,40],
        [10,0,40],
        [10,0,10],
        [40,0,10],
        [50,0,0]
    ]
    for i in coords:
        for j in range(len(i)):
            i[j] = i[j]*scale
        #print i
        i[0]+=(x-w)
        i[2]+=(z-l)
        i[1]*=-1
    #print coords
    return coords

def hill(x,z,w,l,scale=1):
    coords = [
        [0,0,0],
        [0,0,50],
        [50,0,50],
        [50,0,0],
        [0,0,0],
        [20,40,20],
        [50,0,50],
        [50,0,0],
        [20,40,20],
        [0,0,50]
    ]
    for i in coords:
        for j in range(len(i)):
            i[j] = i[j]*scale
        i[0]+=(x-w)
        i[2]+=(z-l)
        i[1]*=-1
    return coords

def water(x,z,w,l,scale):
    coords = [
        [0+x-w,0,0+z-l],
        [0+x-w,5,50+z-l],
        [50+x-w,10,50+z-l],
        [50+x-w,15,0+z-l],
        [0+x-w,0,0+z-l],
        [50+x-w,5,50+z-l],
        [50+x-w,10,0+z-l],
        [0+x-w,5,50+z-l]
            ]
    coords = [
        [0,0,0],
        [0,5,50],
        [50,10,50],
        [50,15,0],
        [0,0,0],
        [50,5,50],
        [50,10,0],
        [0,5,50]
    ]
    for i in coords:
        for j in range(len(i)):
            i[j] = i[j]*scale
        i[0]+=(x-w)
        i[2]+=(z-l)
        i[1]*=-1
    return coords

def movewater(world):
    wind = 2.5
    for line in range(len(world)):
        for index in range(len(world[line])):
            char = world[line][index]
            if char[2] == 'w':
                if char[3][0]>3 and char[3][1]==1:
                    char[3][1] = -1
                    char[3][0] = 0
                if char[3][0]>3 and char[3][1]==-1:
                    char[3][1] = 1
                    char[3][0] = 0
                for i in char[0][5:-1]:
                    i[1]+=wind*char[3][1]
                char[3][0]+=1

def movetree(world):
    wind = 1
    for line in range(len(world)):
        for index in range(len(world[line])):
            char = world[line][index]
            if char[2] == 't':
                if char[3][0]>3 and char[3][1]==1:
                    char[3][1] = -1
                    char[3][0] = 0
                if char[3][0]>3 and char[3][1]==-1:
                    char[3][1] = 1
                    char[3][0] = 0
                for i in char[0][7:-1]:
                    i[0]+=wind*char[3][1]
                char[3][0]+=1
        
def generate(w,l,scale=1):
    world = []
    sw = (600-50*w*scale)/4#300-50*w/2*scale
    sl = (400-50*l*scale)/4#200-50*l/2*scale
    for wIndex in range(w):
        line = []
        for lIndex in range(l):
            item = random.choice(['t','m','w','h'])
            #item = 'p'
            data = 0
            if item == 't':
                obj = tree(wIndex*50*scale,lIndex*50*scale,sw,sl,scale)
                color = [200,255,200]
                data = [0,1]
            if item == 'm':
                obj = hill(wIndex*50*scale,lIndex*50*scale,sw,sl,scale)
                color = [222,184,135]
            if item == 'w':
                obj = water(wIndex*50*scale,lIndex*50*scale,sw,sl,scale)
                color = [200,200,255]
                data = [0,1]
            if item == 'h':
                obj = house(wIndex*50*scale,lIndex*50*scale,sw,sl,scale)
                color = [255,200,255]
            line.append([obj,color,item,data])
        world.append(line)
    return world

def rescale(world,scale):
    newworld = []
    w = 600
    l = 300
    sw = (600-50*w*scale)/4#300-50*w/2*scale
    sl = (400-50*l*scale)/4
    for wIndex in range(len(world)):
        line = []
        for lIndex in range(len(world[wIndex])):
            item = world[wIndex][lIndex][2]
            for line in range(len(world[wIndex][lIndex][0])): 
                for i in range(len(world[wIndex][lIndex][0][line])):
                    world[wIndex][lIndex][0][line][i]*=scale

def main():
    scale = 1
    world = generate(7,7,1)
    xrotate = 0
    yrotate = 0
    zrotate = 0
    offset = [0,0]
    movex = 0
    movey = 0
    highlighted = []
    radians = 0.1/scale
    #print world
    while True:
        threed.clearscreen()
        movewater(world)
        movetree(world)
        radians = 0.1/scale
        for line in world:
            for item in line:
                threed.draw(item[0],item[1],offset)
        for k in world:
            for j in k: threed.rotateX(j[0],xrotate)   
        for k in world:
            for j in k: threed.rotateY(j[0],yrotate)
        for k in world:
            for j in k: threed.rotateZ(j[0],zrotate)
        offset[0]+=movex
        offset[1]+=movey
        for i in pygame.event.get():
            if i.type == QUIT:
                pygame.quit()
            if i.type == KEYDOWN:
                if i.key == K_UP:
                    xrotate = radians
                if i.key == K_DOWN:
                    xrotate = -radians
                if i.key == K_LEFT:
                    yrotate = radians
                if i.key == K_RIGHT:
                    yrotate = -radians
                if i.key == K_g:
                    zrotate = radians
                if i.key == K_b:
                    zrotate = -radians
                if i.key == K_w:
                    movey = 10
                if i.key == K_s:
                    movey = -10
                if i.key == K_a:
                    movex += 10
                if i.key == K_d:
                    movex -= 10
                if i.key == K_f:
                    scale+=radians
                    rescale(world,1.1)
                if i.key == K_v:
                    scale-=radians
                    rescale(world,0.9)
            if i.type == KEYUP:
                xrotate = 0
                yrotate = 0
                zrotate = 0
                movex = 0
                movey = 0
        threed.fpsclock.tick(10)
main()
