# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:17:32 2024

@author: Student
"""

#Tinhgiaithua
n = int(input("Nhap so nguyen duong n:"))
if n > 0:
    giaithua = 1
    for i in range(1,n+1):
        giaithua = giaithua*i
        print(giaithua)
        