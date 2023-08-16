#!/usr/bin/env python3

def greet_programmer():
    return 'Hello, programmer!\n'

def greet(name):
    return f'Hello, {name}!'

def greet_with_default(name='programmer!\n'):
    return f"Hello, {name}!"

def add(num1, num2):
    return num1 + num2
               
def halve(number):
    if not isinstance(number, (int, float)):
        return None
    return number / 2
