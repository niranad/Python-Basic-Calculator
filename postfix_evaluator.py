# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 14:50:28 2022

@author: Adeniran J. Olukanni
"""

from infix_to_postfix import InfixToPostfix


def calculate(y, operator, x):
    if operator == '+':
        return y + x
    elif operator == '-':
        return y - x
    elif operator == '*':
        return y * x
    elif operator == '//':
        return y // x
    elif operator == '/':
        return y / x
    elif operator == '^':
        return y ** x
    elif operator == '%':
        return y % x


def evaluate(postfix):
    postfix_stack = postfix.split()
    postfix_stack += [')']
    postfix_iter = iter(postfix_stack)
    next_str = postfix_iter.__next__()
    eval_stack = []

    while next_str != ')':
        if next_str[0].isdigit():
            eval_stack += [float(next_str)]
        else:
            x = eval_stack.pop()
            
            if len(eval_stack) == 0:
                if next_str != '-' and next_str != '+':
                    return None
            
            y = eval_stack.pop() if len(eval_stack) != 0 else 0
            eval_stack += [calculate(y, next_str, x)]
        
        next_str = postfix_iter.__next__()

    return eval_stack.pop()


class PostfixEvaluator:
    def __init__(self):
        self.postfix = InfixToPostfix().postfix
        if self.postfix is not None:
            result = evaluate(self.postfix)
            print('Result: ', 
                  result if result is not None else 'Error: incomplete expression')
            