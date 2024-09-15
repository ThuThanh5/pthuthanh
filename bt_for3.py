# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:36:29 2024

@author: Student
"""

import random
#20-30
so1 = random.randint(20, 30)
so2 = [random.uniform(18, 99)**2 for i in range(so1)]
print(f"So luong phan tu trong danh sach la: {so1}")
for j in so2:
      print(f"Danh sach cac gia tri binh phuong: {j:.2f}")
      




    
    

