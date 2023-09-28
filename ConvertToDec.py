def convert_remainder (remainder):
    higher_coefs = {"a":10,"b":11,"c":12,"d":13,"e":14,"f":15 }
    if remainder not in higher_coefs:
        return str (remainder)
    else:
        return higher_coefs [remainder]




def convert_hex_to_int(n):
    
    converted_n = ""

    for i in n:
        
        converted_n += str(convert_remainder (i))

    return converted_n

print(convert_hex_to_int("1438aef4"))