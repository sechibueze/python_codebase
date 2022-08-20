
num1 = input("Enter your first number :")
num2 = input("Enter your second number :")

try:
    average = (float(num1) + float(num2)) / 2
    print("The average number is : ", average)
except:
    print("There is an error with the calculation")
    print("Please check your input")
    exit()

# Program will only proceed if there is no error
print("program completed successfully")



