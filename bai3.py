# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:01:44 2024

@author: Student
"""

N=int(input("Nhap so nguyen N có hai chu so="))
if N<10 and N>99:
    print("Không hợp lệ")
else: 
    print ("Tổng các chữ số N=",N//10+N%10)
