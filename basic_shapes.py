from point import Point

import numpy as np

class Plane(object):

    def __init__(self, a, p):
        s = a/2
        self.p1 = Point(p.x+s, -p.y, p.z-s, p.dist)
        self.p2 = Point(p.x-s, -p.y, p.z-s, p.dist)
        self.p3 = Point(p.x-s, -p.y, p.z+s, p.dist)
        self.p4 = Point(p.x+s, -p.y, p.z+s, p.dist)

        self.vertices = [self.p1, self.p2, self.p3, self.p4]

    def rotate_z(self, angle):
        theta = np.radians(angle)
        for vertex in self.vertices:
            vertex.t_rotatez(theta)

    def rotate_y(self, angle):
        theta = np.radians(angle)
        for vertex in self.vertices:
            vertex.t_rotatey(theta)

    def rotate_x(self, angle):
        theta = np.radians(angle)
        for vertex in self.vertices:
            vertex.t_rotatex(theta)

    def translate(self, x, y, z):
        for vertex in self.vertices:
            vertex.translate(x, y, z)
    
    def getcenter(self):
        self.cx = (self.p1.x + self.p2.x + self.p3.x + self.p4.x)/4
        self.cy = (self.p1.y + self.p2.y + self.p3.y + self.p4.y)/4
        self.cz = (self.p1.z + self.p2.z + self.p3.z + self.p4.z)/4

    def bringtocenter (self, cx, cy, cz):
        self.distx = cx
        self.disty = cy
        self.distz = cz
        for vertex in self.vertices:
            vertex.translate(-self.distx, -self.disty, -self.distz)
    
    def bringback (self):
        for vertex in self.vertices:
            vertex.translate(self.distx, self.disty, self.distz)

    def get_procoor(self):
        return self.vertices