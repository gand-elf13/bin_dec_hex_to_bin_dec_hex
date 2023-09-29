from ConvertToDec import convert_to_dec

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
    while True:
        result, remainder = divmod (int (n), 16)
        converted_n += convert_remainder (remainder)
        if result == 0:
            break
        n = result
    return converted_n [::-1] # Reverses the string by slicing

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