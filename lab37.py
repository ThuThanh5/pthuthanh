# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 15:16:24 2024

@author: PHAM THU THANH
"""

n = int(input("Nhập vào số nguyên dương chẵn n: "))
if n > 0 and n % 2 == 0:
    S = sum(i for i in range(2, n + 1, 2))
    print(f"Tổng S từ 2 đến {n} là: {S}")
else:
    print("Số nhập vào phải là số chẵn và lớn hơn 0.")