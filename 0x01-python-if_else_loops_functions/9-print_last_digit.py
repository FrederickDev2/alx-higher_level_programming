#!/usr/bin/python3

def print_last_digit(number):
    last_number = 0
    if number < 0:
        number = number * -1
        last_number = number % 10
        print(last_number, end="")
        return last_number
    else:
        print(number % 10, end="")
        return number % 10
