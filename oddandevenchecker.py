#Create a function to check if a number is even or odd
def even_or_odd(number):
    # Use the modulo operator (%) to find the remainder when dividing by 2
    if number % 2 == 0:
        # If remainder is 0, the number is even
        return "Even"
    else:
        # Otherwise, it is odd
        return "Odd"

# Example 
# initialize a number to check
num = 7
print(f"The number {num} is", even_or_odd(num))

