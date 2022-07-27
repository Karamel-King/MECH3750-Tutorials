# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 13:38:50 2022

@author: samee
"""
import numpy as np


def forward_difference(f,x,h):
    approx = (f(x+h)-f(x))/h
    return approx

def backward_difference(f,x,h):
    approx = (f(x+h)-f(x))/h
    return approx

def central_difference(f,x,h):
    approx = (f(x+h)-f(x))/h
    return approx

def func_a(x):
    return x**3

def func_b(x):
    return 3*x**2 - 2*x

def func_c(x):
    return np.sin(x)
