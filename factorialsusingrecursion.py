# create a function that calculates the factorial of a number using recursion
def factorial_recursive(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: multiply n by factorial of (n-1)
        return n * factorial_recursive(n - 1)

# Example 
number = 5
print(f"Factorial of {number} is", factorial_recursive(number))
