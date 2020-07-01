import tkinter
import basic_shapes
import point
import threading
import random
import time

from tkinter import Canvas

root = tkinter.Tk()

c = Canvas(master=root, width=800, height=800, bg='black')
c.pack()

def draw_plane(pointlist):
    for p in range(-1, len(pointlist)-1):
        c.create_line(pointlist[p].prox+400, pointlist[p].proy+400, pointlist[p+1].prox+400, pointlist[p+1].proy+400, fill='white', width=2)

theta = 0

planelist = []

for i in range(4):
    plane = basic_shapes.Plane(100, point.Point(0, 50, 0, 300))
    plane.rotate_z(theta)
    pointlist = plane.get_procoor()
    draw_plane(pointlist)
    planelist.append(plane)
    theta += 90
    #make a cube instead

def bringtocenter ():
    cx = 0
    cy = 0
    cz = 0

    for plane in planelist:
        plane.getcenter()
        cx += plane.cx
        cy += plane.cy
        cz += plane.cz

    cx /= 4; cy /= 4; cz /= 4

    for plane in planelist:
        plane.bringtocenter(cx, cy, cz)
        

def rotate_anim():
    a = 5.0
    while(a > 0):
        c.delete('all')
        for plane in planelist:
            plane.rotate_y(1)
            plane.rotate_z(-1)
            plane.rotate_x(1)
            pointlist = plane.get_procoor()
            draw_plane(pointlist)
        a -= 0.02
        time.sleep(0.02)

def move(x, y, z):
    c.delete('all')
    for plane in planelist:
        plane.translate(x, y, z)
        pointlist = plane.get_procoor()
        draw_plane(pointlist)

def rotate(x, y, z):
    c.delete('all')
    bringtocenter()
    for plane in planelist:
        plane.rotate_x(x)
        plane.rotate_y(y)
        plane.rotate_z(z)

        plane.bringback()
        
        pointlist = plane.get_procoor()
        draw_plane(pointlist)

def key(event):
    speed = 10
    if event.char == "w":
        move(0, 0, speed)
    if event.char == "s":
        move(0, 0, -speed)
    if event.char == "a":
        move(-speed, 0, 0)
    if event.char == "d":
        move(speed, 0, 0)
    if event.char == "o":
        move(0, -speed, 0)
    if event.char == "p":
        move(0, speed, 0)
    if event.char == "j":
        rotate(5, 0, 0)
    if event.char == "k":
        rotate(0, 5, 0)
    if event.char == "l":
        rotate(0, 0, 5)

root.bind("<Key>", key)

root.mainloop()