from ConvertToDec import convert_to_dec


'''
reverse_str is a function that takes a string s,
and returns it reversed, using a slicing method
'''
def reverse_str (s):
    return s [::-1]


'''
convert_remainder is a function that takes the remainder (int),
converts it to a hexadecimal notation, and returns it (string).
'''
def convert_remainder (remainder):
    higher_coefs = {
        10 : "a",
        11 : "b",
        12 : "c",
        13 : "d",
        14 : "e",
        15 : "f",
    }
    if remainder < 10:
        return str (remainder)
    else:
        return higher_coefs [remainder]


'''
convert_dec_to_hex is a function that takes a string n
(containing a number in decimal notation), that
converts it to a hexadecimal notation, and that
returns it (as a string)
'''
def convert_dec_to_hex (n):
    converted_n = ""
    is_negative = int (n) < 0
    if is_negative:
        n = n [1:]
    while True:
        result, remainder = divmod (int (n), 16)
        converted_n += convert_remainder (remainder)
        if result == 0:
            break
        n = result
    
    converted_n = reverse_str (converted_n)
    if is_negative:
        converted_n = "-" + converted_n
    return converted_n


'''
convert_bin_to_hex is a function that takes a string b
(containing a binary number), converts it to hexadecimal,
and returns it (as a string)
'''
def convert_bin_to_hex (b):
    n = convert_to_dec (b, "bin")
    return convert_dec_to_hex (n)


'''
convert_to_hex is a function that takes a string n, and 
a string called base. This function converts n in
hexadecimal depending on the string base.
It returns ultimately a string containing the hexadecimal
notation of n.
'''
def convert_to_hex (n, base):
    if base == "dec":
        return convert_dec_to_hex (n)
    elif base == "bin":
        return convert_bin_to_hex (n)
    elif base == "hex":
        return str (n)
    else:
        return f"ERROR : {base} IS NOT A SUPPORTED BASE YET. IT FUNCTIONS ONLY FOR bin/dec/hex BASES ONLY"


if __name__ == "__main__":
    print(convert_to_hex("-1988971", "dec"))
    print(convert_to_hex("1ae867f987d", "hex") == "1ae867f987d")
    print(convert_to_hex("100100101", "bin") == "125")