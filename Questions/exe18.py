# The function sum_positive_numbers should return the sum of all positive numbers 
# between the number n received and 1. For example, when n is 3 it should return 1+2+3=6, 
# and when n is 5 it should return 1+2+3+4+5=15. Fill in the gaps to make this work:

def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return n

    # The recursive case is adding this number to 
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n - 1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

"""
Additional Recursion Sources
In the past videos, we visited the basic concepts of recursive functions.

A recursive function must include a recursive case and base case. The recursive case calls the function again, with a different value. The base case returns a value without calling the same function.

A recursive function will usually have this structure:

def recursive_function(parameters):
    if base_case_condition(parameters):
        return base_case_value
    recursive_function(modified_parameters)
"""