#!/bin/python3
import time

t0 = time.time()
from pyth import *

from numpy import array, rot90, ones, trace, array_equal, transpose, zeros
from sys import argv

lines = [bin(i)[2:].zfill(6) for i in range(2 ** 6)]
lines = [[int(i) for i in list(line)] for line in lines if sum([int(i) for i in line]) == 3]

def numberToBase(n, b):
    if n == 0: return [0] * 6
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    l = digits[::-1]
    if len(l) < 6:
        zzz = [0] * (6 - len(l))
        l = zzz + l
    return l

def areDuplicate(s1, s2):
    if array_equal(s1, s2): return True
    s2 = rot90(s2)
    if array_equal(s1, s2): return True
    s2 = rot90(s2)
    if array_equal(s1, s2): return True
    s2 = rot90(s2)
    if array_equal(s1, s2): return True
    s2 = transpose(s2)
    if array_equal(s1, s2): return True
    s2 = rot90(s2)
    if array_equal(s1, s2): return True
    s2 = rot90(s2)
    if array_equal(s1, s2): return True
    s2 = rot90(s2)
    if array_equal(s1, s2): return True
    return False

def isDuplicateTo(square, collection):
    if len(collection) == 0: return False
    for item in collection:
        if areDuplicate(square, item): return True
    return False

def isSemi(square, n):
    square = rot90(square)
    for line in square:
        if sum(line) != n: return False
    return True

def isMagic(square, n):
    if not isSemi(square, n): return False
    if trace(square) != n: return False
    square = rot90(square)
    if trace(square) != n: return False
    return True

t1 = time.time()
total = t1-t0
print(str(total) + '\n')





print('generating binary magic square generators')

dbmsgens = []
for i in range(64000000):
    i = array([lines[line] for line in numberToBase(i, 20)])
    if isMagic(i, 3):
        dbmsgens.append(i)

print(str(dbmsgens[0]))

print('saving binary magic square generators')

f = open('dbmsgens.txt', 'w')
f.write(str(dbmsgens))
f.close()

t1 = time.time()
total = t1 - t0
print(str(total) + '\n')



# print('loading duplicate binary magic square generators')
# f = open('dbmsgens.txt', 'r')
# dbmsgens = eval(''.join(f.readlines()))
# f.close()



print('generating transitional squares')

dtsquares = dbmsgens[:]
abcdef = [0,1,2,2,1,0]
for i in range(len(dtsquares)):
    for line in range(6):
        for cell in range(6):
            if dtsquares[i][line][cell]: dtsquares[i][line][cell] = abcdef[cell]
            else: dtsquares[i][line][cell] = 5 - abcdef[cell]
print(str(dtsquares[0]))

print('saving transitional squares')

f = open('dtsquares.txt', 'w')
f.write(str(dtsquares))
f.close()

t1 = time.time()
total = t1 - t0
print(str(total) + '\n')





print('generating duplicate full squares')

dfsquares = dtsquares[:]
dfsquares = [6 * s + rot90(s) + ones((6, 6)) for s in dfsquares]
print(dfsquares[0])

print('saving duplicate full squares')

f = open('dfsquares.txt', 'w')
f.write(str(dfsquares))
f.close()

t1 = time.time()
total = t1 - t0
print(str(total) + '\n')




print('filtering for unique squares')
dfusquares = []
for s in dfsquares:
    p = list(chain(*s))
    p.sort()
    if p == [i for i in range(1, 37)]: dfusquares.append(s)
    else: dfusquares.append(zeros((6, 6)))
print(dfusquares[0])

print('saving duplicate full unique squares')

f = open('dfusquares.txt', 'w')
f.write(str(dfusquares))
f.close()

t1 = time.time()
total = t1 - t0
print(str(total) + '\n')




print('filtering for magic squares')
dfumsquares = []
for s in dfusquares:
    if isMagic(s, 111): dfumsquares.append(s)
    else: dfumsquares.append(zeros((6, 6)))
print(dfumsquares[0])

print('saving duplicate full unique magic squares')

f = open('dfumsquares.txt', 'w')
f.write(str(dfumsquares))
f.close()

t1 = time.time()
total = t1 - t0
print(str(total) + '\n')




print('look up duplicate binary magic square generators')
f = open('dbmsgens.txt', 'r')
dbmsgens = eval(''.join(f.readlines()))
f.close()

dgbmsquares = []

for i in range(len(dfumsquares)):
    if isMagic(dfumsquares[i], 111): dgbmsquares.append(dbmsgens[i])
    else: dgbmsquares.append(zeros((6, 6)))
print(dgbmsquares[0])

print('saving duplicate binary magic square generators')

f = open('dgbmsquares.txt', 'w')
f.write(str(dgbmsquares))
f.close()

t1 = time.time()
total = t1 - t0
print(str(total) + '\n')




print('removing duplicate cases')
ubmsgens = []
for square in dgbmsquares:
    if isMagic(square, 3):
        if not isDuplicateTo(square, ubmsgens):
            ubmsgens.append(square)
print(ubmsgens[0])

print('saving unique binary generators')

f = open('ubmsgens.txt', 'w')
f.write(str(ubmsgens))
f.close()

t1 = time.time()
total = t1 - t0
print(str(total) + '\n')

unique = ubmsgens