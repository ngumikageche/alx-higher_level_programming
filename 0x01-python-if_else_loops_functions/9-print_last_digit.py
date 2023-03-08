#!/usr/bin/python3
def print_last_digit(number):
   if number < 0:
          positive = number * -1
          l_digit = positive % 10
          print("{}".format(l_digit), end="")
          return(l_digit)
   else:
          l_digit = number % 10
          print("{}".format(l_digit), end="")
