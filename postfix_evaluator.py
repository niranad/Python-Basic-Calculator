# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 14:50:28 2022

@author: Temitope A. Abdul
"""

from infix_to_postfix import InfixToPostfix


def calculate(y, operator, x):
    if operator == '+':
        return y + x
    elif operator == '-':
        return y - x
    elif operator == '*':
        return y * x
    elif operator == '/':
        return y / x
    elif operator == '//':
        return y // x
    elif operator == '^':
        return y ** x
    elif operator == '%':
        return y % x


def evaluate(postfix):
    postfix_stack = postfix.split()
    postfix_stack += [')']
    postfix_iter = iter(postfix_stack)
    next_str = ''
    eval_stack = []

    while next_str != ')':
        next_str = postfix_iter.__next__()
        if next_str[0].isdigit():
            eval_stack += [float(next_str)]
        else:
            if len(eval_stack) != 0:  
                x = eval_stack.pop()
                if len(eval_stack) == 0:
                    return x
                y = eval_stack.pop()
                eval_stack += [calculate(y, next_str, x)]

    return eval_stack.pop()


def _format():
    pass


class PostfixEvaluator:
    def __init__(self):
        self.postfix = InfixToPostfix().postfix
        if self.postfix is not None:
            print('Result: ', evaluate(self.postfix))
        
