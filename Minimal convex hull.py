import numpy as np
import matplotlib.pyplot as plt
import math



def cmp2(x1, y1):

    x = x1 - p0[0]
    y = y1 - p0[1]
    if x > 0 and y >= 0:
        return abs(math.atan(y / x))
    if x > 0 and y < 0:
        return abs(math.atan(y / x) + 2 * math.pi)
    if x < 0:
        return abs(math.atan(y / x) + math.pi)
    if x == 0 and y > 0:
        return abs(math.pi / 2)
    if x == 0 and y < 0:
        return abs(3 * math.pi / 2)

def rotate(a, b, c):
  return (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0]-b[0]) < 0


A = [(2, 2), (4, 4), (2, 4), (4, 2), (2.5, 3), (4, 6), (-5, -5), (-8, -5), (4.5, 3),
(6, 8.5), (-105, 6), (-100, 0), (100, 2)]
A2 = A
n = len(A)
print(A2)
p0 = (min(A, key = lambda x: x[1] or x[1] and x[0]))
A.remove(p0)
A.sort(key = lambda x: cmp2(x[0], x[1]))
#print(p0)
#print(A)
stack = [p0, A[0]]
A.pop()
#print(stack)
for pt in A:
    while(rotate(stack[-2], stack[-1], pt)):
        del stack[-1]
    stack.append(pt)
print(stack)
"""""
stack.append(stack[0])

fig = plt.figure()
import random
Xs = []
Ys = []
for x in A2:
    Xs.append(x[0])
    Xs.append(x[1])
plt.plot(Xs, Ys, 'ro')
fig.show()
Xs2 = []
Ys2 = []
for x in stack:
    Xs.append(x[0])
    Xs.append(x[1])
plt.plot(Xs2, Ys2, 'g-')
fig.show()
"""

