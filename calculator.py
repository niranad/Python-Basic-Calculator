# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 15:31:11 2022

@author: Adeniran J. Olukanni
"""

from postfix_evaluator import PostfixEvaluator

print('--------Welcome to HiQ Basic Python Calculator---------\
      \nSigns\n+ add\n- subtract\n* multiply\n/ divide\
      \n// floor division\n^ power\n% modulus\n')
      

calculator = PostfixEvaluator()
quit_calc = True if calculator.postfix is None else False

while quit_calc is False:
    calculator = PostfixEvaluator()
    quit_calc = True if calculator.postfix is None else False
else:
    print('Good bye')


