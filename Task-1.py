#Task-1
#Making a function to calculate the  factorial 
def factorial(n):
    if n < 0:
        return "Cannot find factorial. Please enter a positive number"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n=int(input("Enter a Number to calculate factorial: "))
answer = factorial(n)
print("Factorial of", n, "is", answer)