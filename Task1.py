def factorial(num):
    multi=1
    for i in range(1,num+1):
        multi *= i
    return multi
n = int(input("Enter a number: "))
print(f"Factorial of {n} is:",factorial(n))