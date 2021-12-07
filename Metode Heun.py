# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 14:22:19 2021

@author: faris
"""
# Metode Heun
# Definisikan fungsi f(x)
def f(x,y):
    return -2*x*y**2
# Euler Method
def heun(x0,y0,xn,n):
    # Menghitung ukuran langkah xi
    h = (xn-x0)/n
    
    print('--------------------')
    print('x0\ty0\tfxy\tyn')
    print('--------------------')
    for i in range(n):
        k1 = h * f(x0,y0)
        k2 = h * (f((x0+h),(y0+k1)))
        k = (k1 + k2)/2
        yn = y0 + k
        print('%.4f\t%.4f\t%.4f'% (x0,y0,yn))
        print('--------------------')
        y0 = yn
        x0 = x0+h
    print('\nJadi x=%.4f, y=%.4f' %(xn,yn))
# Input
print('\nMasukan Kondisi Awal: ')
x0 = float(input('x0 = '))
y0 = float(input('y0 = '))
print('Masukan Titik yang akan du Hitung: ')
xn = float(input('xn = '))
print('\Masukan Jumlah Iterasi: ')
step = int(input('Jumlah Iterasi = '))
# Memanggil Method Heun
heun(x0,y0,xn,step)