#!/usr/bin/env python
#coding: utf-8

'''

 SIMULATION
 Fibonacci numbers

'''
n = int(input("Enter a number: "))

f1=0
f2=1

if(n==0 ):
	print (0)
	
else:
	for i in range (0,n):
		f1 = f1 + f2
		f2 = f1 - f2
		print(f2)