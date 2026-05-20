# This script is a calculator simulation
import operator

# ask user to input two numbers and store it in a variable
number1 = float(input("Input the first number: "))
number2 = float(input("Input second number: "))

# ask user to determine an operation
operation = input("Choose an operation (+, -, *, /): ")

# set a dictionary which will hold string operators as keys and an operator method as a value
operation_dict = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

# store the answer in a variable, the operator method and the two numbers
answer = operation_dict[operation](number1, number2)

# print user inputs in a readable string
print(f"{number1} {operation} {number2} = {answer}")