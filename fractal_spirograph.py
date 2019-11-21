#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 19:21:36 2019

@author: daniel
"""

import matplotlib.pyplot as plt
plt.ion()
from matplotlib import animation
import numpy as np


class Circle:
    def __init__(self, x = 0, y = 0, r = 10, n = 0, parent = None, ratio = 3.0, resolution = 1, k = -4.0):
        self.r = r
        self.x = x
        self.y = y
        self.n = n
        self.resolution = np.float(resolution)
        self.k = k
        self.v = np.radians(self.k ** (self.n - 1)) / self.resolution
        self.angle = np.pi / 2
        self.parent = parent
        self.child = None
        self.ratio = ratio
        
    def add_child(self):
        new_r = self.r / self.ratio
        new_x = self.x + self.r + new_r
        new_y = self.y
        self.child = Circle(x=new_x, y=new_y, r=new_r, n= self.n+1,  parent = self)
        return self.child
    def update(self):     
        if self.parent:
            self.angle += self.v
            rsum = self.r + self.parent.r
            self.x = self.parent.x + rsum * np.cos(self.angle)
            self.y = self.parent.y + rsum * np.sin(self.angle)
            
            
    def show(self, ax):
        ax.add_artist(plt.Circle([self.x, self.y], self.r, edgecolor = "gray", facecolor = "none", lw = 0.5 ))
        

def init():
    global circles
    global xdata, ydata
    global base
    global k
    base = Circle(resolution=resolution, n=0, ratio= division_rate, k = k)
    circle = base
    for x in range(n_circles):
        circle = circle.add_child()
    line.set_data(xdata, ydata)
    return line,

def animate(i):
    global xdata
    global ydata
    global base  
    ax.clear()
    ax.axis("equal")
    ax.set_xlim(-base.r - 20,base.r +20)
    ax.set_ylim(-base.r - 20,base.r +20)
    ax.set_title(str(i)) 
    
    for step in range(resolution):
        circle = base
        while True:
            circle.update()
            if step == resolution-1:
               circle.show(ax)
            if circle.child != None:
                circle = circle.child
            else:
                break
        xdata = np.append(xdata, circle.x)
        ydata = np.append(ydata, circle.y)


    line, = ax.plot(xdata, ydata, c = "r", lw = 0.1)
    fig.canvas.draw()
    return line,

global resolution
global n_circles
global division_rate
global k
if __name__ == "__main__":
    resolution = 1
    n_circles = 10
    division_rate = 3.0
    k = 4
    
    xdata = np.array([])
    ydata = np.array([])
    fig, ax = plt.subplots(figsize = (5,5))
    line, = ax.plot(xdata, ydata, c = "r", lw = 1)
    ani = animation.FuncAnimation(fig, animate, init_func=init, interval = 1, repeat = True, blit = True)
    plt.show()
#    ani.save("spiro_detail.gif", writer = "imagemagick", fps = 30)
#    plt.close()