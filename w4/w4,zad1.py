import numpy as np
import matplotlib.pyplot as plt 
def los_mac(n):
    return np.random.choice([0,255],n*n, p =[0.5, 0.5]).reshape(n,n)

def addGlider(i, j, grid):
    glider = np.array([[0, 0, 255], [255, 0, 255], [0, 255, 255]])
    
    rx = glider.shape[0]
    ry = glider.shape[1]
    
    grid[i:i+rx, j:j+ry] = glider
    return grid

def addBlock(i, j, grid):
  
    block = np.array([[255, 255],  
                       [255,  255]])
    rx = glider.shape[0]
    ry = glider.shape[1]
    
    grid[i:i+rx, j:j+ry] = block 
    return grid

