# -*- coding: utf-8 -*-
""" Created on Sat Feb  3 20:33:51 2018
@author: krishna.i
Assignment 2.3: Write a Python program to reverse a word after accepting the
input from the user.

Sample Output:
    Input word: AcadGild
    Output: dilGdacA

"""

aname= str(input("Enter a word: "))
print("Input word: ",aname)
revname = aname[::-1]
print("Output: ",revname)
# End of the code