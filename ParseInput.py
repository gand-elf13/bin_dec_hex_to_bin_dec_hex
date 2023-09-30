from ConvertToDec import convert_to_dec
from ConvertToBin import convert_to_bin
from ConvertToHex import convert_to_hex


'''
wait_for_input is a function that is very useful to get correct input,
in a way that keeps the software and program robust and that rids any
input bugs. It is a function that takes a text to display before getting input,
an error text in case the input doesn't fit the possible inputs the user
could have input, and a variadic string argument which corresponds
to the possible user inputs.
It returns the correct user input (type string)
'''
def wait_for_input (text, error_text, *possible_inputs):
    current_input = input (text)
    while current_input not in possible_inputs:
        print (error_text)
        current_input = input (text)
    return current_input


'''
is_binary is a function that takes a string n.
It checks whether that string is a binary number,
by checking if the length of that string is equal to
the sum of the char counts of "0" and "1"
(since binary numbers are made of "0"s and "1"s)
It returns a bool.
'''
def is_binary (n):
    return len (n) == (n.count ("0") + n.count ("1"))
    
    
'''
is_decimal is a function that takes a string n.
It checks whether that string is a decimal number
by checking that every character is a digit.
It returns a bool.
'''
def is_decimal (n):
    for char in n:
        if char not in "0123456789":
            return False
    return True
    

'''
is_hexadecimal is a function that takes a string n.
It checks if that string is a hexadecimal number by
checking every character.
It returns a bool.
'''
def is_hexadecimal (n):
    for char in n:
        if char.lower () not in "0123456789abcdef":
            return False
    return True


'''
is_input_valid is a function that checks if the input number n (type string)
and if the initial_base (type string) is valid/fitting.
As it checks, it returns a bool.
'''
def is_input_valid (n, initial_base):
    if initial_base == "dec":
        return is_decimal (n)
    elif initial_base == "hex":
        return is_hexadecimal (n)
    elif initial_base == "bin":
        return is_binary (n)
    else:
        return False


'''
get_n_and_base is a function that takes no argument and that returns
two strings : n and initial_base.
'''
def get_n_and_base ():
    while True:
        n = input ("Insert the number : ")
        initial_base = wait_for_input (
            "Insert the number's base (dec/bin/hex) : ",
            "ERROR, INITIAL BASE IS NOT SUPPORTED YET",
            "dec", "bin", "hex",
        )
        if is_input_valid (n, initial_base):
            break
        else:
            print ("ERROR, THE INPUT NUMBER DOESN'T FIT ITS BASE")
    return n, initial_base
    

'''
get_inputs is a function that takes no arguments,
that returns three strings : n, initial_base, final_base.
This function gets and returns all necessary user's input.
'''
def get_inputs ():
    n, initial_base = get_n_and_base ()
    final_base = wait_for_input (
        "To which base do you want to conver this number? (dec/bin/hex) : ",
        "ERROR, FINAL BASE IS NOT SUPPORTED YET",
        "dec", "bin", "hex"
    )
    return n, initial_base, final_base


'''
output_result is a function that takes 3 arguments
(string n, initial_base, final_base) and outputs
the result of the number base conversion. As such,
it returns None.
'''
def output_result (n, initial_base, final_base):
    final_n = ""
    if final_base == "hex":
        final_n = convert_to_hex (n, initial_base)
    elif final_base == "dec":
        final_n = convert_to_dec (n, initial_base)
    elif final_base == "bin":
        final_n = convert_to_bin (n, initial_base)
    print (f"The number {n} ({initial_base}) in {final_base} base is : {final_n}")
    
    
    
    
