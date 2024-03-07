# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 10:00:20 2024

@author: Student
"""

import math
radius=float(input("請輸入元的半徑:"))
circumference= 2 * math.pi * radius
area=math.pi *(radius ** 2)
print(f"半徑為{radius},周長為:{circumference:.2f},面積為:{area:.2f}")