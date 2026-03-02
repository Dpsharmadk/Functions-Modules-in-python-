#Task-1
#Making a function to calculate the  factorial 
def factorial(n):
    result = 1
    if n <= 0:
        print("Cannot find factorial. Please enter a positive number") #we are checking if the number is greater than zero and then we wil find its factorial 
    else:
        for i in range(1,n+1):
            result *= i
        return result

n=int(input("Enter a Number to calculate factorial: "))
answer = factorial(n)
print("Factorial of", n, "is", answer)