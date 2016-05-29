#!/usr/bin/env python
# https://www.hackerrank.com/challenges/python-lists
# harshil912@gmail.com 


count = raw_input()
items = []
for i in range(int(count)):
    command = raw_input().split(' ')
    if command[0] == 'append':
        items.append(int(command[1]))
    # if command[0] == 'extend':
        
    if command[0] == 'insert':
        items.insert(int(command[1]), int(command[2]))
    if command[0] == 'remove':
        items.remove(int(command[1]))
    if command[0] == 'pop':
        items.pop()
    if command[0] == 'index':
        print items.index(int(command[1]))
    if command[0] == 'count':
        print items.count(int(command[1]))
    if command[0] == 'sort':
        items.sort()
    if command[0] == 'reverse':
        items.reverse()
    if command[0] == 'print':
        print items

