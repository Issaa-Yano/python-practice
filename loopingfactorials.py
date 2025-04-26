# create a function to compute factorial using a loop
def factorial_loop(n):
    # Start with result as 1 (since factorial starts multiplying from 1)
    result = 1
    # Loop from 1 to n (inclusive)
    for i in range(1, n + 1):
         # Multiply result by the current number in the loo
        result *= i 
        # After the loop ends, return the final factorial value 
    return result

# Example
#initializing a number to calculate its factorial
number = 5
print(f"Factorial of {number} is", factorial_loop(number))

