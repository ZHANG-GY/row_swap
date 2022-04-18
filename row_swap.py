# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 18:27:53 2022

@author: 13687
"""

import numpy as np
A = np.arange(25).reshape(5,5)
print(A)

B = A[[4,1,2,3,0],:]
print(B)