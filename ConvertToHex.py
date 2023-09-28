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


def convert_dec_to_hex (n):
    converted_n = ""
    while True:
        result, remainder = divmod (int (n), 16)
        converted_n += convert_remainder (remainder)
        if result == 0:
            break
        n = result
    return converted_n [::-1]


def convert_bin_to_hex (b):
    n = int (b, 2) # WE WILL USE MAXIME'S FUNCTIONS WHEN AVAILABLE
    return convert_dec_to_hex (n)


# MAIN FUNCTION
# THIS SHOULD BE THE ONLY FUNCTION THAT'S EXECUTED FROM THIS FILE!!!
def convert_to_hex (n, base):
    if base == "dec":
        return convert_dec_to_hex (n)
    elif base == "bin":
        return convert_bin_to_hex (n)
    elif base == "hex":
        return str (n)
    else:
        return f"ERROR : {base} IS NOT A SUPPORTED BASE YET. IT FUNCTIONS ONLY FOR bin/dec/hex BASES ONLY"
