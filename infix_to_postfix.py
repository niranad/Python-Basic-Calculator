# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 14:48:11 2022

@author: Adeniran J. Olukanni
"""

import re


def get_infix():
    """Returns a calculation expression read from the user at the keyboard."""
    infix = input('Enter an expression to calculate or otherwise to quit: \n')
    return infix


def format_infix(infix):
    """Removes spaces from the input expression and replaces fragments of the 
    expression such as 5( and )3 with 5*( and )*3."""
    infix = infix.replace(' ', '')
    match1 = re.search('(\\)\\d+)', infix)
    match2 = re.search('(\\d+\\()', infix)

    if type(match1) is re.Match:
        num1str = match1.group().replace(')', '')
        infix = re.sub('(\\)\\d+)', ')*' + num1str, infix)

    if type(match2) is re.Match:
        num2str = match2.group().replace('(', '')
        infix = re.sub('(\\d+\\()', num2str + '*(', infix)

    return infix


def is_operator(string):
    """Returns true if the input string arg is an operator, false otherwise."""
    operator_pat = '[+*/%^-]'
    return True if re.search(operator_pat, string) else False


def precedence(op):
    """Returns a precedence value for the following operators: + - * / ^ %"""
    if op == '+' or op == '-':
        return 0
    elif op == '*' or op == '/' or op == '//' or op == '%':
        return 1
    elif op == '^':
        return 2


def validate_infix(infix):
    """Checks if the input expression is a valid infix."""
    wrong_infix_pat = '[^\\d()+*%/^.\\s-]|(\\+\\+)|(\\-\\-)|(\\*\\*)|(\\%\\%)|(\\^\\^)|(\\.\\.)'
    parens = re.findall('\\(|\\)', infix)
    left_parens = []
    right_parens = []

    for i in range(len(parens)):
        if parens[i] == '(':
            left_parens += [parens[i]]
        else:
            right_parens += [parens[i]]

    if re.search(wrong_infix_pat, infix) or \
        len(left_parens) != len(right_parens):
        return False
    else:
        return True


def to_postfix(formatted_infix):
    """Converts a formatted infix expression to postfix."""
    if formatted_infix == '':
        return None
    
    if validate_infix(formatted_infix):
        infix_stack = []

        for m in re.finditer('([+*%^()-])|(\\/{1,2})|\\d+(\\.\\d+)?', formatted_infix):
            infix_stack += [m.group()]

        infix_stack += [')']
        print('infix-stack: ', infix_stack)
        infix_iter = iter(infix_stack)

        stack = []
        stack += ['(']

        postfix = ''

        while len(stack) != 0:
            _next = infix_iter.__next__()
            if _next[0].isdigit():
                postfix += _next + ' '
            elif _next == '(':
                stack += [_next]
            elif is_operator(_next):
                while is_operator(stack[len(stack) - 1]) and \
                        precedence(stack[len(stack) - 1]) >= precedence(_next):
                    postfix += stack.pop() + ' '
                stack += [_next]
            elif _next == ')':
                while stack[len(stack) - 1] != '(':
                    postfix += stack.pop() + ' '
                stack.pop()

        return postfix
    else:
        return None


class InfixToPostfix:
    """Reads an expression from the user at the keyboard, format, validate and convert it to a
    postfix expression if expression is a valid infix"""
    def __init__(self):
        self.postfix = to_postfix(format_infix(get_infix()))
