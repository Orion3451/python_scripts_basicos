#!/usr/bin/env python
# -*- coding: utf-8 -*-

import turtle

def main():
    window = turtle.Screen()
    tortuguin = turtle.Turtle()

    crear_cuadrado(tortuguin)
    turtle.mainloop()

def crear_cuadrado(x):
    medida = int(raw_input('Tamaño del cuadrado: '))
    for i in range(4):
        crear_linea_girar(x, medida )

def crear_linea_girar(x, y):
    x.forward(y)
    x.left(90)

if __name__ =='__main__':
    main()
