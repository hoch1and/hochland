#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from tkinter import *
from queue import PriorityQueue
import math


n = 750
r = 50
tile = 12
w = r * tile
h = r * tile
barrier = np.random.randint(1, r - 1, [2, n])

window = Tk()
window.title('Algorithm A*')
canvas = Canvas(window, width = w, height = h, bg = 'white')

for k in range(n):
    canvas.create_oval(barrier[0][k] * tile + (1/4 * tile), barrier[1][k] * tile + (1/4 * tile),
                       barrier[0][k] * tile + (3/4 * tile), barrier[1][k] * tile + (3/4 * tile),
                       fill = 'black')

def is_barrier(x, y):
    return any(barrier[0][k] == x and barrier[1][k] == y for k in range(n))

def heuristic(a, b):
    (x1, y1), (x2, y2) = a, b
    return math.hypot(x2 - x1, y2 - y1)

def get_neighbors(pos):
    (x, y) = pos
    results = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1),
               (x + 1, y + 1), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1)]
    neighbors = filter(lambda x: not is_barrier(*x), results)
    return neighbors

def draw_tile(pos, color):
    x, y = pos
    canvas.create_rectangle(x * tile, y * tile, x * tile + tile, y * tile + tile, fill = color, outline = '')

def redraw_path(came_from, current, previous_path):
    for item in previous_path:
        canvas.delete(item)
    new_path = []
    while current in came_from:
        next_node = came_from[current]
        if next_node:
            item = canvas.create_line((current[0] * tile + tile/2, current[1] * tile + tile/2,
                                       next_node[0] * tile + tile/2, next_node[1] * tile + tile/2),
                                       fill = 'purple', width = tile/3)
            new_path.append(item)
        current = next_node
    window.update()
    return new_path

def a_star(start, goal):
    draw_tile((0, 0), '#F1CECE')
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {}
    current_weight = {}
    came_from[start] = None
    current_weight[start] = 0
    previous_path = []

    while True:
        current = frontier.get()[1]

        if current == goal:
            redraw_path(came_from, current, previous_path)
            break
        
        for i in get_neighbors(current):
            new_weight = current_weight[current] + heuristic(current, i)
            if i not in current_weight or new_weight < current_weight[i]:
                current_weight[i] = new_weight
                priority = new_weight + heuristic(goal, i)
                frontier.put((priority, i))
                came_from[i] = current
                draw_tile(i, '#F1CECE')
                previous_path = redraw_path(came_from, i, previous_path) # Восстановление и стирание пути
                window.after(1)

start_button = Button(window, text = 'Algorithm A*', command = lambda: a_star((0, 0), (r - 1, r - 1)))
start_button.pack()

canvas.pack()
window.mainloop()


# In[ ]:




