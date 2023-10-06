from ConvertToDec import convert_to_dec
from ConvertToBin import convert_to_bin
from ConvertToHex import convert_to_hex


'''
wait_for_input is a function that is made to get user's input,
in a more bug-robust way. It basically prints a text,
gets user's input, and if the user's input is in one of
the possible supported inputs, then it is returned.
Otherwise, the function prints an error text and gets user's input
until the input is a supported one.
This function takes 2 strings (text, error_text) and a variadic number
of following arguments (*possible_inputs) corresponding to
the different available inputs that the user can choose.
'''
def wait_for_input (text, error_text, *possible_inputs):
    current_input = get_input (text)
    if current_input == "EXIT":
        print ("PROGRAM IS NOW EXITING")
        quit ()
    while current_input not in possible_inputs:
        print (error_text)
        current_input = get_input (text)
    return current_input


'''
is_binary is a function that checks if a string is a binary number.
Since binary notation only uses zeros and ones, the sum of the number of "0"
and "1" in a string should be equal to its length, in case the string really
is a binary number.
is_binary takes a string n, and returns a bool
'''
def is_binary (n):
    return len (n) == (n.count ("0") + n.count ("1"))


'''
is_decimal is a function that checks if a string is
a decimal number by checking if every character
is a digit.
is_decimal takes a string n and returns a bool.
'''
def is_decimal (n):
    for char in n:
        if char not in "0123456789":
            return False
    return True


'''
is_hexadecimal is a function that checks if a string is a hexadecimal number,
by checking if every character is in
"0123456789abcdef" (the hexadecimal different coefficients).
is_hexadecimal takes a string n and returns a bool
'''
def is_hexadecimal (n):
    for char in n:
        if char.lower () not in "0123456789abcdef":
            return False
    return True


'''
is_input_valid is a function that checks if the user's input
fits its base.
is_input_valid takes two strings : n and initial_base,
and returns a bool.
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
get_n_and_base is a function that gets user's input number
and its base.
It takes no arguments, and returns two strings: n and initial_base
'''
def get_n_and_base ():
    while True:
        n = get_input ("Insert the number : ")
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
get_input is a function that takes a string text
and returns the user input, unless the user
input 'EXIT' which makes the program exit.
'''
def get_input (text):
    i = input (text)
    if i == "EXIT":
        quit ()
    return i
'''
get_inputs is a function that gets all necessary user's inputs.
It takes no arguments, and returns three strings :
n, initial_base and final_base
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
    print ("The number %s (%s) in %s base is %s" % (n, initial_base, final_base, final_n))



