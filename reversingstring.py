# create a function that reverses a string manually without using slicing or built-in functions
def reverse_string(s):
    # Create an empty string to store the reversed result
    reversed_str = ''
    
    # Loop through each character in the input string
    for char in s:
        # Add each character at the beginning of the reversed string
        reversed_str = char + reversed_str
    
    # Return the reversed string
    return reversed_str

# Example 
my_string = "hello"
print("Reversed string:", reverse_string(my_string))
