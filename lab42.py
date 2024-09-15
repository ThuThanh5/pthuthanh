# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 15:31:02 2024

@author: PHAM THU THANH
"""

def tinh_tong(n):
  tong = 0
  for i in range(1, n+1):
    tong += 1/i - 1/(i+1)
  return tong
n = int(input("Nhập số lượng số hạng n: "))
ket_qua = tinh_tong(n)
print("Tổng của dãy số là:", ket_qua)