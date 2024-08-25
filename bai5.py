# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:35:32 2024

@author: Student
"""

N=int(input("Nhập năm sinh:"))
if N>2024:
    print("Không hợp lệ")
else:
    print("Bạn sinh năm",N,"vậy bạn",2024-N,"tuổi")