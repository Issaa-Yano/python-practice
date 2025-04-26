# Create a function to add all elements in a list
def sum_list(numbers):
    # Start with total as 0
    total = 0
    # Loop through each number in the list
    for num in numbers:
    # Add each number to total
        total += num  
    return total

# Example usage
#intialise a list of numbers
my_list = [1, 2, 3, 4, 5]
print("Sum of the list:", sum_list(my_list))
