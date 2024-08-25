# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:13:42 2024

@author: Student
"""

h=int(input("Nhập giờ:"))
p=int(input("Nhập phút:"))
g=int(input("Nhập giây:"))
var1=h*3600
print("Đổi giờ ra giây=",var1)
var2=p*60
print("Đổi phút ra giây",var2)
var3=var1+var2+g
print("Tổng=",var3)