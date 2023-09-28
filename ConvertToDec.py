def convert_remainder (remainder):
    higher_coefs = {"a":10,"b":11,"c":12,"d":13,"e":14,"f":15 }
    if remainder not in higher_coefs:
        return str (remainder)
    else:
        return higher_coefs [remainder]




def convert_hex_to_int(n):
    
    converted_n = 0
    power = 0

    for i in reversed(n):
        
        converted_n =converted_n + (int(convert_remainder(i))*(16**power))
        power += 1
    return converted_n


def convert_bin_to_int(n):
    
    converted_n = 0
    power = 0

    for i in reversed(n):
        
        converted_n =converted_n + (int(i)*(2**power))
        power += 1
    return converted_n


print(convert_bin_to_int("10010011"))