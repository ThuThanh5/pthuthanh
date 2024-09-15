# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 15:32:20 2024

@author: PHAM THU THANH
"""

a, b, c, n = 2, 7, 9, 979
solutions = []
for x in range(1, n // a + 1):
    for y in range(1, (n - a * x) // b + 1):
        if (n - a * x - b * y) % c == 0:
            z = (n - a * x - b * y) // c
            if z > 0:
                solutions += [(x, y, z)]
print("Các bộ nghiệm nguyên của phương trình là:")
for sol in solutions:
    print(sol)