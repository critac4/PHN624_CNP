import numpy as np
import matplotlib
import matplotlib.pyplot as plt 
import scipy

def Z_val(A):
    if A%2 == 0: return A/2 
    if A%2 == 1: return (A-1)/2 
    if A==1: return 1 
    else: return -1 

def BE(A, Z):
    binEg=15.75*A - 17.8*(A**(2/3)) - 23.7*(((A-2*Z)**2)/A) - 0.71*((Z**2)/A**(1/3)) + Del(A,Z)
    return binEg/A
    
def Del(A, Z):
    if Z%2==0: 
        return 33.5/(A**(3/4))
    if A%2==1:
        return 0
    if Z%2==1:
        return -33.5/(A**(3/4))
    else: return -1
    
#plotting the BE v A 

A = np.arange(1, 251)
#print(A) 
for i in A:
    Z = Z_val(i)    
    Binding_Energy=BE(i, Z)
    BE=np.append(Binding_Energy)
plt.plot(A, Binding_Energy)
plt.show