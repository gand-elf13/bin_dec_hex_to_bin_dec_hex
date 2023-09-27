import library




def convert_hex_to_dec(n):
    
    converted_n = ""

    while True:
        result , remainder = divmod(n , 2)
        converted_n += library.convert_remainder (remainder)

        if result == 0:
            break
        n = result
    return converted_n [::-1]

print(convert_hex_to_dec("a"))