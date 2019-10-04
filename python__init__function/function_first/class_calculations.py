import sys
# appending the path of another folder
sys.path.insert(0,'../')
from function_second import functions_for_classcalculation

# creating two variables for operations
variable1 = 4
variable2 = 3

# creating the object of the class FunctionsForClassFirst
calculation_object = functions_for_classcalculation.FunctionsForClassFirst(variable1, variable2)

# addition of two numbers
addition = calculation_object.addition()
print("Addition of {} and {} is:".format(variable1, variable2), addition)

# subtraction of two numbers
subtraction = calculation_object.subtraction()
print("Subtraction of {} and {} is:".format(variable1, variable2), subtraction)

# division of two numbers
division = calculation_object.division()
print("Division of {} and {} is:".format(variable1, variable2), division)

# multiplication of two numbers
multiply = calculation_object.multiplication()
print("Multiplication of {} and {} is:".format(variable1, variable2), multiply)