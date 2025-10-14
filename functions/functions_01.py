"""
This module demonstrates the basics of defining and using functions in Python.
It includes two simple functions that print messages to indicate their execution flow.
Each function has no parameters and does not return any value.
The functions are called sequentially to show how they operate independently.
"""


# Defining a simple function with no parameters and no return value
def start_function_1():
    print("\nFunction 1 started...")
    print("Function 1 in progress...")
    print("Function 1 completed.")
    print("Function 1 ended.")


# Defining another function
def start_function_2():
    print("\nFunction 2 started...")
    print("Function 2 in progress...")
    print("Function 2 completed.")
    print("Function 2 ended.")


# Calling the functions
start_function_1()
start_function_2()