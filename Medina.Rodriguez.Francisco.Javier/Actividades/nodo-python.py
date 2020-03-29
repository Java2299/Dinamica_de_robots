#!/usr/bin/env python 
# encoding: utf-8

def nodo(): 	
	mensaje = "Hola mundo"
	print(mensaje)
	
if __name__ == '__main__':
		try:
			nodo()
		except:
			print("una excepción ha ocurrido") 	
