# -*- coding: utf-8 -*-
"""newton_raphson_for_root_finding.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Aabinv2oNNDpdJ_aBjz3UBVo5WwuxnWf
"""

#sympy library is imported to ease calculations with symbols
from sympy import *
x = symbols('x')

#The function f is defined along with its first derivative
f = x**5 - 15*x**4 + 85*x**3 - 225*x**2 + 274*x - 120
f1 = f.diff(x)

#initialisation of a few variables
abs_err = 0.001   #maximum error allowed
max_iter = 10000   #maximum number of iterations allowed
i = 0             #initialising iteration variable i

#x_old denotes the starting value of x given
x_old = 3.5
err = x_old

#Running the loop to get approximation of the root
#This root acts as the point where the function f(x) cuts the x-axis
#Since the polynomial is of degree 5, there are 5 roots in total
old = x_old

#We run the loop either till the err value becomes less than the maximum allowed
#error value or till we complete max_iter number of iterations
while err >= abs_err and i < max_iter :

  #Calculating the value of first and second derivatives of f at x = old
  f_val = f.subs(x, old)
  f1_val = f1.subs(x, old)

  #Preventing division by zero
  if f1_val == 0 :
    break

  #We get a new value of x by applying Newton Raphson method
  x_new = old - f_val/f1_val

  #Calculating the value of first derivative of f at x = x_new
  newf_val = f.subs(x, x_new)

  #updating the variables for the next iteration
  err = abs(newf_val - f_val)
  old = x_new
  i += 1
#end while

#Printing the output
print("The function is given by - ")
print(f)
print("\nThe first derivative of the function is given by - ")
print(f1)
print("\nWith the starting value as ", x_old, ", the new value is: ")
print (old)

"""Some alternative outputs - 

With the starting value as  0.5 , the new value is: 
1.00000000000000

With the starting value as  1.0 , the new value is: 
1.00000000000000

With the starting value as  1.5 , the new value is: 
1.99999999784676

With the starting value as  2.0 , the new value is: 
2.00000000000000

With the starting value as  2.5 , the new value is: 
5.00000000000000

With the starting value as  2.8 , the new value is: 
3.00000000000005

With the starting value as  3.0 , the new value is: 
3.00000000000000

With the starting value as  3.3 , the new value is: 
3.00000000000000

With the starting value as  3.5 , the new value is: 
1.00000000000000

With the starting value as  4.0 , the new value is: 
4.00000000000000

With the starting value as  4.5 , the new value is: 
4.00000000215317

With the starting value as  5.0 , the new value is: 
5.00000000000000

With the starting value as  5.5 , the new value is: 
4.99999999999994

With the starting value as  6.0 , the new value is: 
5.00000000000018

With the starting value as  0.01 , the new value is: 
0.999999999999970
"""