# This script is a calculator simulation
import operator
import re

# use regex pattern matching to figure out if a number is valid or not to be floated. ^ - must start with either a - or . or 0 or more nums, float will still work without a num before a decimal / * is 0 or more / it has to end with at least one number though if there's a decimal which is what the + and $ is for
number_pattern = r"^[-]?[0-9]*[.]?[0-9]+$"

# ask user to input two numbers and store it in a variable    
input_number1 = input("Input the first number: ")
# check if it's valid with the match, if it is do nothing
if re.match(number_pattern, input_number1) == None:
    print(f"The number you typed, {input_number1}, is not valid. Please try again!")
    quit()

input_number2 = input("Input second number: ")

if re.match(number_pattern, input_number2) == None:
    print(f"The number you typed, {input_number2}, is not valid. Please try again!")
    quit()

# set a dictionary which will hold string operators as keys and an operator method as a value
operation_dict = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}
# ask user to determine an operation
operation = input("Choose an operation (+, -, *, /): ")

# if it's not a key in the dictionary, it's not valid
if not operation in operation_dict:
    print(f"The operation you typed, {operation}, is not valid. Please try again!")
    quit()

# store the answer in a variable, the operator method and the two numbers
answer = operation_dict[operation](float(input_number1), float(input_number2))

# print user inputs in a readable string
print(f"{input_number1} {operation} {input_number2} = {answer}")