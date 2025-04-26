# Create a function that calculates the sum of the digits of a number
def sum_of_digits(n):
    # Initialize total sum as 0
    total = 0
    
    # Loop until all digits are processed
    while n > 0:
        # Add the last digit (n % 10) to the total
        total += n % 10
        
        # Remove the last digit from the number (integer division by 10)
        n = n // 10
    
    # Returns the total sum of digits
    return total

# Example 
number = 1234
print("Sum of digits:", sum_of_digits(number))
