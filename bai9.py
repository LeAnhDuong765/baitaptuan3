# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:27:07 2024

@author: Student
"""
print("Tính giá trị biểu thức")
a=float(input("Nhập số a:"))
b=float(input("Nhập số b:"))
S=(a**(1/2) - b**(1/2))/(a**(1/4) - b**(1/4)) - ((a**(1/2) + (a*b)**(1/4))/(a**(1/4) + b**(1/4)))
print("Giá trị biểu thức=",S)