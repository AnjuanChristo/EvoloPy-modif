# -*- coding: utf-8 -*-
"""
Created on Tue May 17 12:46:20 2016

@author: Hossam Faris
"""

import numpy as np
import math
from scipy.io import loadmat
from basic_functions import fsphere, fgriewank, frastrigin, fackley, fweierstrass
from scipy.optimize import minimize

# define the function blocks
def prod(it):
    p = 1
    for n in it:
        p *= n
    return p

def LSM(weights):
    comparison_matrix = np.array([[1, 8, 8, 6],
                            [1/8, 1, 7, 1/5],
                            [1/8, 1/7, 1, 1/8],
                            [1/6, 5, 8, 1]])
    n = len(weights)
    obj_value = 0
    for i in range(n):
        for j in range(n):
            obj_value += (comparison_matrix[i][j] - weights[i] / weights[j])**2
            
    penalty_factor = 100
    penalty_term = penalty_factor * (np.sum(weights) - 1)**2
    return obj_value + penalty_term
    
def getFunctionDetails(a):
    # [name, lb, ub, dim]
    param = {
        "LSM":["LSM", 0, 1, 4],
    }
    return param.get(a, "nothing")

'''
# ESAs space mission design benchmarks https://www.esa.int/gsp/ACT/projects/gtop/
from fcmaes.astro import (
    MessFull,
    Messenger,
    Gtoc1,
    Cassini1,
    Cassini2,
    Rosetta,
    Tandem,
    Sagas,
)
def Ca1(x):
    return Cassini1().fun(x)
def Ca2(x):
    return Cassini2().fun(x)
def Ros(x):
    return Rosetta().fun(x)
def Tan(x):
    return Tandem(5).fun(x)
def Sag(x):
    return Sagas().fun(x)
def Mef(x):
    return MessFull().fun(x)
def Mes(x):
    return Messenger().fun(x)
def Gt1(x):
    return Gtoc1().fun(x)

def getFunctionDetails(a):
    # [name, lb, ub, dim]
    param = {
        "F1": ["F1", -100, 100, 2],
        "F2": ["F2", -10, 10, 2],
        "F3": ["F3", -100, 100, 2],
        "F4": ["F4", -100, 100, 2],
        "F5": ["F5", -30, 30, 2],
        "F6": ["F6", -100, 100, 30],
        "F7": ["F7", -1.28, 1.28, 30],
        "F8": ["F8", -500, 500, 30],
        "F9": ["F9", -5.12, 5.12, 30],
        "F10": ["F10", -32, 32, 30],
        "F11": ["F11", -600, 600, 30],
        "F12": ["F12", -50, 50, 30],
        "F13": ["F13", -50, 50, 30],
        "F14": ["F14", -65.536, 65.536, 2],
        "F15": ["F15", -5, 5, 4],
        "F16": ["F16", -5, 5, 2],
        "F17": ["F17", -5, 15, 2],
        "F18": ["F18", -2, 2, 2],
        "F19": ["F19", 0, 1, 3],
        "F20": ["F20", 0, 1, 6],
        "F21": ["F21", 0, 10, 4],
        "F22": ["F22", 0, 10, 4],
        "F23": ["F23", 0, 10, 4],
        "Ca1": [
            "Ca1",
            Cassini1().bounds.lb,
            Cassini1().bounds.ub,
            len(Cassini1().bounds.lb),
        ],
        "Ca2": [
            "Ca2",
            Cassini2().bounds.lb,
            Cassini2().bounds.ub,
            len(Cassini2().bounds.lb),
        ],
        "Gt1": ["Gt1", Gtoc1().bounds.lb, Gtoc1().bounds.ub, len(Gtoc1().bounds.lb)],
        "Mes": [
            "Mes",
            Messenger().bounds.lb,
            Messenger().bounds.ub,
            len(Messenger().bounds.lb),
        ],
        "Mef": [
            "Mef",
            MessFull().bounds.lb,
            MessFull().bounds.ub,
            len(MessFull().bounds.lb),
        ],
        "Sag": ["Sag", Sagas().bounds.lb, Sagas().bounds.ub, len(Sagas().bounds.lb)],
        "Tan": [
            "Tan",
            Tandem(5).bounds.lb,
            Tandem(5).bounds.ub,
            len(Tandem(5).bounds.lb),
        ],
        "Ros": [
            "Ros",
            Rosetta().bounds.lb,
            Rosetta().bounds.ub,
            len(Rosetta().bounds.lb),
        ],
    }
    return param.get(a, "nothing")
'''
