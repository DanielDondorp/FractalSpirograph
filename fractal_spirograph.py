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
        self.v = np.radians(self.k ** (self.n -1)) / self.resolution
        self.angle = np.pi / 2
        self.parent = parent
        self.child = None
        self.ratio = ratio
        
    def add_child(self):
        new_r = self.r / self.ratio
        new_x = self.x + self.r + new_r
        new_y = self.y
        self.child = Circle(x=new_x, y=new_y, r=new_r, n= self.n+1, ratio = self.ratio, parent = self)
        return self.child
    def update(self):     
        if self.parent:
            self.angle += self.v
            rsum = self.r + self.parent.r
            self.x = self.parent.x + rsum * np.cos(self.angle)
            self.y = self.parent.y + rsum * np.sin(self.angle)
            
            
    def show(self, ax):
        ax.add_artist(plt.Circle([self.x, self.y], self.r, edgecolor = "gray", facecolor = "none", lw = 0.5 ))
        


class Spirograph:
    def __init__(self, n_circles = 10, k = -4, resolution = 100, division_rate = 3.0, 
                 start_radius = 10, frames = 1000, interval = 10, linewidth = 0.1, alpha = 0.5):
        self.n_circles = n_circles
        self.k = k
        self.resolution = resolution
        self.division_rate = division_rate
        self.start_radius = start_radius
        self.frames = frames
        self.interval = interval
        self.linewidth = linewidth
        self.alpha = alpha
        
        self.base = Circle(r=self.start_radius, ratio = self.division_rate, 
                           resolution = self.resolution, k = self.k)
        next_circle = self.base
        for _ in range(self.n_circles):
            next_circle = next_circle.add_child()
        
        self.x_data = np.array([])
        self.y_data = np.array([])
        
    def make_animation(self):
        fig, ax = plt.subplots(figsize = (6,6))
        line, = ax.plot([],[], c = "r", lw = self.linewidth, alpha = self.alpha)
        
        def initialize_plot():
            line.set_data(self.x_data, self.y_data)
            return line,
        
        def animate(i):
            ax.clear()
            ax.axis("equal")
            ax.set_xlim(-self.base.r - 50,self.base.r +50)
            ax.set_ylim(-self.base.r - 50,self.base.r +50)
            ax.set_title(str(i))
            
            for step in range(self.resolution):
                circle = self.base
                while True:
                    circle.update()
                    if step == self.resolution-1:
                        circle.show(ax)
                    if circle.child != None:
                        circle = circle.child
                    else:
                        break
                self.x_data = np.append(self.x_data, circle.x)
                self.y_data = np.append(self.y_data, circle.y)
            
            line, = ax.plot(self.x_data, self.y_data, c = "r", lw = self.linewidth, alpha = self.alpha)
            fig.canvas.draw()
            return line,
        
        anim = animation.FuncAnimation(fig, animate, init_func=initialize_plot, 
                                       blit = True, interval = self.interval, frames = self.frames)
        return anim
    
    def show_animation(self):
        anim = self.make_animation()
        plt.show()
    
    def save_animation(self):
        anim = self.make_animation()
        anim.save("./animated_fractal.gif", writer = "imagamagick")
        
        
        

if __name__ == "__main__":
    s = Spirograph(resolution=5, linewidth =0.5, alpha = 1)
    s.show_animation()
