#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:26:41 2019

@author: yuri
"""

import scipy
from numpy import pi



def Drag ( ro , D , Cd , V ):
    return Cd * ro * V**2 * pi * D**2 / 8






