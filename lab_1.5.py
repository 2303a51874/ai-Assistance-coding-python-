#write python program reverses a given string 
#accepts user input
#implements the logic directly in the main code
#does not use any user-defined functions
if __name__ == "__main__":
    user_input = input("Enter a string to reverse: ")
    reversed_string = user_input[::-1]
    print("Reversed string:", reversed_string)

#examine the copilot-generated code from lab_1.5.py and improve removing unnecessary variables,simplifying loop or indexing logic,improving readability and efficiency
def reverse_string(s):
    return s[::-1]


# generate code from lab_1.5.py
# the string reversal logic is needed in multiple parts of an application,
# uses a user-defined function to reverse a string,
# returns the reversed string,
# include meaningful comments
def reverse_string(s):
    """
    This function takes a string as input and returns the reversed string.
    
    Parameters:
    s (str): The string to be reversed.
    
    Returns:
    str: The reversed string.
    """
    return s[::-1]

#write a code to generate a loop-based string reversal approach,a built-in/slicing-based string reversal approach
def reverse_string_loop(s):
    """
    This function reverses a string using a loop-based approach.
    
    Parameters:
    s (str): The string to be reversed.
    
    Returns:
    str: The reversed string.
    """
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str