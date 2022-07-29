import numpy as np

L = 0.001
d = 5E-6
k = 200
h = 1000
P = np.pi*d
A = (np.pi*d**2)/4

T_a = 293.15
T_4 = 343.15
T_0 = 353.15


def theta(Tx,Ta):
    return Tx - Ta

def lumpedsq(h,P,k,A):
    x=h*P
    y=k*A
    return x/y

def ana_sol(T_a, T_L, T_0, h, P, k, A, L, x):
    Theta_L = theta(T_L, T_a)
    Theta_0 = theta(T_0, T_a)
    lumped = lumpedsq(h,P,k,A)**0.5
    
    numer = Theta_L*np.sinh(lumped*x) + Theta_0*np.sinh(lumped*(L-x))
    domin = np.sinh(lumped*L)
    
    return numer/domin

def theta_array(x,h,P,k,A, T_a, T_4, T_0):
    
    sig = -2 - lumpedsq(h,P,k,A)*x**2
    
    Theta_L = theta(T_4, T_a)
    Theta_0 = theta(T_0, T_a)
    
    b = np.array([Theta_0, 0, 0, 0,Theta_L])
    
    M = np.diag([1,sig,sig,sig,1],0)+np.diag([0,1,1,1],-1)+np.diag([1,1,1,0],1)
    
    theta_array = np.linalg.solve(M,b)
    
    print(theta_array), print(sig), print(M)
    
    return theta_array, sig, M

name = theta_array(0.0002,h,P,k,A, T_a, T_4, T_0)