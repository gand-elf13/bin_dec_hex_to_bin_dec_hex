def wait_for_input (text, error_text, *possible_inputs):
    current_input = input (text)
    while current_input not in possible_inputs:
        print (error_text)
        current_input = input (text)
    return current_input


def is_binary (n):
    return len (n) == (n.count ("0") + n.count ("1"))
    
    
def is_decimal (n):
    for char in n:
        if char not in "0123456789":
            return False
    return True
    
    
def is_hexadecimal (n):
    for char in n:
        if char.lower () not in "0123456789abcdef":
            return False
    return True


def is_input_valid (n, initial_base):
    if initial_base == "dec":
        return is_decimal (n)
    elif initial_base == "hex":
        return is_hexadecimal (n)
    elif initial_base == "bin":
        return is_binary (n)
    else:
        return False

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

def get_inputs ():
    n, initial_base = get_n_and_base ()
    final_base = wait_for_input (
        "To which base do you want to conver this number? (dec/bin/hex) : ",
        "ERROR, FINAL BASE IS NOT SUPPORTED YET",
        "dec", "bin", "hex"
    )
    print(n, initial_base, final_base)


get_inputs()