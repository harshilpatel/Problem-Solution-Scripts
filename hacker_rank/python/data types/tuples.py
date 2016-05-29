#!/usr/bin/env python
# https://www.hackerrank.com/challenges/python-tuples?h_r=next-challenge&h_v=legacy

count = int(raw_input())

items = [ int(i) for i in raw_input().split() ]

print(hash(tuple(items)))