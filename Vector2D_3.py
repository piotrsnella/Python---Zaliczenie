import numpy as np 
import math

class Vector2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "x={}, y={}".format(self.x, self.y)
        
    def modul(self):
        lenght = ((self.x)**2 + (self.y)**2)**0.5
        return lenght
    
    def zwieksz(self, x, y):
        self.x = self.x + x
        self.y = self.y + y
        
    def zmniejsz(self, x, y):
        self.x = self.x - x
        self.y = self.y - y
        
    def mnozenie(self,a):
        self.x = self.x * a
        self.y = self.y * a
        
    def translacja(self):
        pass
    
    def il_skal(self, x, y):
        iloczyn = self.x* x + self.y * y
        return iloczyn
    
    def obroc(self, A):
        arg_x = self.x* math.cos(A*(math.pi/180)) - self.y* math.sin(A*(math.pi/180))
        arg_y = self.x* math.sin(A*(math.pi/180)) + self.y* math.cos(A*(math.pi/180))
        return arg_x, arg_y



        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    