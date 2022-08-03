# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 13:06:36 2022

@author: samee
"""

def factorial(n):
    #return n!
    output = 1
    for term in range(1,n+1):
        output *= term
    return output

def exptaylor(n,x):
    #Return Taylor Series of exp(x) using n terms
    # exp(x)=
    #       1       =1/fact(0) * x**0
    #       + 1     =1/fact(1) * x**1
    #       + x**2  =1/fact(2) * x**2
    
    #               =1/fact(term) * x**term
    output = 0
    for term in range(0,n+1):
        output += 1/factorial(term) * x**term
    return output


def better_exp(n,x):
    # exp(x)=
    #       1       =1/fact(0) * x**0
    #       + 1     =1/fact(1) * x
    #       + x**2  =1/fact(2*1) * x*x
    
    #               =1/fact(term) * x**term
    term = 1 
    output = term
    for i in range(1,n+1):
        term *= x / i
        output += term
    
    return output












