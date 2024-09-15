# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 15:15:46 2024

@author: PHAM THU THANH
"""

n = int(input("Nhập vào số nguyên dương n: "))
if n > 0:
    S = sum(range(1, n + 1))
    print(f"Tổng S từ 1 đến {n} là: {S}")
else:
    print("Số nhập vào không phải là số nguyên dương.")