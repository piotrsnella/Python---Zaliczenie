import numpy as np
import math 

class Matrix():
    def __init__(self, m, n):
        self.m = m 
        self.n = n
        self.body = []
        
    def wypelnij(self):
        self.body = []
        for i in range(m):
            init_list =[]
            for j in range(n):
                element - float(input("aij = "))
                init_list.append(element)
                
            self.body.append(init_list)                
            
    def ones(self):
        self.body = []
        for i in range(self,m):
            init_list =[]
            for j in range(self,n):
                element = 0
                init_list.append(element)
                
    def unit(self):
        if(self.m == self.n):
            self.body = []
            for i in range(self.m):
                init_list = []
                