import sys
sys.stdin = open('input.txt')
print(*range(int(input()),0,-1),sep='\n')