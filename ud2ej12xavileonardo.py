#!/usr/bin/env python
# -*- coding: utf-8 -*-
s=0
r=0
m=0
d=0
resultado=0
def suma(a,b):
	resultado=a+b
	return resultado
def resta(a,b):
	resultado=a-b
	return resultado
def multiplicacion(a,b):
	resultado=a*b
	return resultado
def division(a,b):
	resultado=a/b
	return resultado
print "S,R,M,D"
print "introduce un numero"
a=int(input())
print "introduce otro numero"
b=int(input())
print "introduce una letra"
letra=raw_input()
while letra<>"si":
	print "el resultado es"
	if letra=="s":
		print suma(a,b)
	if letra=="r":
		print resta(a,b)
	if letra=="m":
		print multiplicacion(a,b)
	if letra=="d":
		print division(a,b)
	print "introduce una letra"
	letra=raw_input()
if letra=="si":
	print "se ha acabado el programa"
 




	
	
	
