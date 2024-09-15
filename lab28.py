# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 15:10:09 2024

@author: PHAM THU THANH
"""

N = int(input("Nhập vào một số nguyên dương N: "))
while N <= 0:
    print("N phải là số nguyên dương. Vui lòng nhập lại!")
    N = int(input("Nhập vào một số nguyên dương N: "))
print(f"Các ước số của {N} là:")
for i in range(1, N + 1):
    if N % i == 0:
        print(i)