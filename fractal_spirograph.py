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
    def __init__(self, x = 0, y = 0, r = 10, n = 0, parent = None):
        self.r = r
        self.x = x
        self.y = y
        self.n = n
        self.v = np.radians(-4.0 ** (self.n - 1))
        if n%2==0:
            self.v *= -1.0
        self.angle = -np.pi / 2
        self.parent = parent
        self.child = None
    def add_child(self):
        new_r = self.r / 3.0
        new_x = self.x + self.r + new_r
        new_y = self.y
        self.child = Circle(x=new_x, y=new_y, r=new_r, n= self.n+1, parent = self)
        return self.child
    def update(self):
        
        if self.parent:
            rsum = self.r + self.parent.r
            self.x = self.parent.x + rsum * np.cos(self.angle)
            self.y = self.parent.y + rsum * np.sin(self.angle)
            
            self.angle += self.v
    def show(self, ax):
        ax.add_artist(plt.Circle([self.x, self.y], self.r, edgecolor = "k", facecolor = "none"))
        

def init():
    global circles
    global xdata, ydata
    global base
    base = Circle()
    circle = base
    for x in range(100):
        circle = circle.add_child()
#    ax.add_artist(plt.Circle([base.x, base.y], base.r, edgecolor = "k", facecolor = "none"))
#    circles = []
#    circle = base
#    for i in range(10):
#        circle = circle.add_child()
#        circles.append(circle)
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
    circle = base
    while True:
        circle.update()
        circle.show(ax)
        if circle.child != None:
            circle = circle.child
        else:
            break
        
#        ax.add_artist(plt.Circle([circle.x, circle.y], circle.r))
        
    xdata = np.append(xdata, circle.x)
    ydata = np.append(ydata, circle.y)  
    line, = ax.plot(xdata, ydata, c = "r", lw = 0.5)
#    base_artist = plt.Circle([base.x, base.y], base.r, edgecolor="k", facecolor="None")
#    ax.add_artist(base_artist)
#    for s in circles:
#        c = plt.Circle([s.x, s.y], s.r, edgecolor = "k", facecolor = "None")
#        ax.add_artist(c)
#        s.update()

    fig.canvas.draw()
    return line,

if __name__ == "__main__":
    xdata = np.array([])
    ydata = np.array([])
    fig, ax = plt.subplots(figsize = (5,5))
    line, = ax.plot(xdata, ydata, c = "r", lw = 1)
    ani = animation.FuncAnimation(fig, animate, init_func=init, interval = 1, frames = 500, repeat = False, blit = True)
#    plt.show()
    ani.save("spiro.mp4", fps = 30)
#    plt.close()