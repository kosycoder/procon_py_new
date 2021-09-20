import numpy as np

x = input()
x1 = int(x[0])
x2 = int(x[1])
x3 = int(x[2])
x4 = int(x[3])

cond1 = 0
cond2 = 0

if(x1==x2):
    cond1 += 1
if(x2==x3):
    cond1 += 1
if(x3==x4):
    cond1 += 1
if(np.remainder(x1+1,10)==np.remainder(x2,10)):
    cond2 += 1
if(np.remainder(x2+1,10)==np.remainder(x3,10)):
    cond2 += 1
if(np.remainder(x3+1,10)==np.remainder(x4,10)):
    cond2 += 1

if(cond1==3 or cond2==3):  
    print("Weak")
else:
    print("Strong")
