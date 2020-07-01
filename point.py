import numpy as np

class Point(object):

    def __init__(self, x, y, z, dist):
        self.x = x
        self.y = y
        self.z = z
        self.position = np.array([x, y, z, 1])

        self.dist = dist

        self.project()

    def project (self):
        self.proz = self.dist/(self.dist + self.z)
        self.prox = self.x*self.proz
        #self.proy = (self.y*self.proz*self.dist)/(np.abs(self.x)+self.dist)
        self.proy = self.y*self.proz

    def t_rotatez(self, theta):
        matrix = np.array([[np.cos(theta), np.sin(theta), 0, 0], [-np.sin(theta), np.cos(theta), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        matrix = np.transpose(matrix)

        transformation = np.matmul(self.position, matrix)
        self.x = transformation[0]  #Add a number here to translate in x
        self.y = transformation[1] 
        self.z = transformation[2] 
        self.position = transformation
        self.project()

    def t_rotatey(self, theta):
        matrix = np.array([[np.cos(theta), 0, -np.sin(theta), 0], [0, 1, 0, 0], [np.sin(theta), 0, np.cos(theta), 0], [0, 0, 0, 1]])
        matrix = np.transpose(matrix)

        transformation = np.matmul(self.position, matrix)
        self.x = transformation[0]  #Add a number here to translate in x
        self.y = transformation[1]
        self.z = transformation[2] 
        self.position = transformation
        self.project()

    def t_rotatex(self, theta):
        matrix = np.array([[1, 0, 0, 0], [0, np.cos(theta), np.sin(theta), 0], [0, -np.sin(theta), np.cos(theta), 0], [0, 0, 0, 1]])
        matrix = np.transpose(matrix)

        transformation = np.matmul(self.position, matrix)
        self.x = transformation[0] #Add a number here to translate in x
        self.y = transformation[1]
        self.z = transformation[2]
        self.position = transformation
        self.project()

    def translate(self, x, y, z):
        self.x += x
        self.y += y
        self.z += z
        self.position = np.array([self.x, self.y, self.z, 1])

        self.project()