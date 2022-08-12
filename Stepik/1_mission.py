# 1 mission
from math import *

n = int(input())
if log2(n) > int(log2(n)):
    print(int(log2(n) + 1))
else:
    print(log2(n))