# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 14:03:28 2021

@author: Muhammad Faris 202010225262 TF3A6
"""
# Metode Euler
# Mendefinisikan fungsi f(x)
def f(x,y):
    return -2*x*y**2
# Euler mthod
def euler(x0,y0,xn,n):
    # MWnghitung ukuran langkah xi
    h = (xn-x0)/n
    print('---------------------------------')
    print('x0\ty0\tfxy\tyn')
    print('---------------------------------')
    for i in range(n):
        fxy = f(x0, y0)
        yn = y0 + h * fxy
        print('%.4f\t%.4f\t%0.4f\t%.4f'% (x0,y0,fxy,yn))
        print('-----------------------------------')
        y0 = yn
        x0 = x0+h
    print('\nJadi x=%.4f, y=%.4f' %(xn,yn))
# Inputs
print('\nMasukan Kondisi awal: ')
x0 = float(input('x0 = '))
y0 = float(input('y0 = '))

print('\nMasukan Titik yang di hitung: ')
xn = float(input('xn = '))

print('\nMasukan Jumlah Iterasi: ')
step = int(input('jumlah Iterasi = '))

# Euler method call
euler(x0,y0,xn,step)