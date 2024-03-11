# create a simple python program to swap variables using three variables

var1 = int(input("Enter the value of variable 1: "))
var2 = int(input("Enter the value of variable 2: "))
# Temporary variable
var3 = 0

# swapping logic using three variables

var3 = var1
var1 = var2
var2 = var3

# output the swapping variables
print("After swapping: ")
print(f"Variable 1: {var1}")
print(f"Variable 2: {var2}")

# create a simple python program to swap variables using two variables

var1 = int(input("Enter the value of variable 1: "))
var2 = int(input("Enter the value of variable 2: "))

# swapping logic using three variables
var1, var2 = var2, var1

# output the swapping variables
print("After swapping: ")
print(f"Variable 1: {var1}")
print(f"Variable 2: {var2}")