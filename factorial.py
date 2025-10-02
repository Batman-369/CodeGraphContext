def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_loop(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

num = int(input("Enter a number: "))
print("Factorial using recursion:", factorial_recursive(num))
print("Factorial using loop:", factorial_loop(num))
