#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from numpy import sin, cos, exp, pi
from scipy import integrate

def user_func(x, func_string):
    return eval(func_string)

# Exceptions:
while True:
    try:
        formula = input("Input function (use 'x' as a variable): ")

       # Scipy
        intg, error = integrate.quad(user_func, 0, np.pi, args=(formula,))  # Args= only accepts tuples!
        print(f"Scipy quad result: {intg:.4f}")

        # Monte Carlo
        N = 100000
        x_vals = np.random.uniform(0, np.pi, N)
        y_vals = user_func(x_vals, formula)
        MC_intg = (np.pi - 0) * np.mean(y_vals)
        print(f"Monte Carlo result: {MC_intg:.4f}")

        break     # If both calculations were succesfully completed

    except NameError:
        print("The variable name can't be recognized, use 'x' and numpy functions.")
    except TypeError:
        print("The type of the inputted object is not appropriate.")
    except SyntaxError:
        print("Error: Your math expression is formatted incorrectly.")

