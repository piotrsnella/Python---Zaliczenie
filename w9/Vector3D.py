import numpy as np
import math

class Vector3D():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __str__(self):
        return "x={}, y={}, z={}".format(self.x, self.y, self.z)
    
    def modul(self):
        lenght = ((self.x)**2 + (self.y)**2 + (self.z)**2)**0.5
        return lenght
    
    def zwieksz(self, x, y, z):
        self.x = self.x + x
        self.y = self.y + y
        self.z = self.z + z
        return self.x, self.y, self.z
        
    def zmniejsz(self, x, y, z):
        self.x = self.x - x
        self.y = self.y - y
        self.z = self.z - z
        return self.x, self.y, self.z
        
    def mnozenie(self,a):
        self.x = self.x * a
        self.y = self.y * a
        self.z = self.z * a
        return self.x, self.y, self.z

        
    def il_skal(self, x, y, z):
        iloczyn = self.x* x + self.y * y + self.z * z
        return iloczyn
        
    def il_wekt(self, x, y, z):
        self.x = self.y * z - self.z * y
        self.y = self.z * x - self.x * z
        self.z = self.x * y - self.y * x
        return self.x, self.y, self.z
    
