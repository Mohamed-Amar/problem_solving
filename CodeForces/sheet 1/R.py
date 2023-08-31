# num = int(input())
# sumi = 0
# for i in range(num + 1):
#     sumi += i
# print(sumi)

import numpy as np

num = int(input())
sumi = sum(np.arange(1, num))
print(sumi)
