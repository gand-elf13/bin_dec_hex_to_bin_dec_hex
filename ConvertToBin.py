# en cas de hex, convertir en dec, puis en bin
# en cas de dec, convertir en bin directement

def convert_dec_to_bin (n):
    converted_n = ""
    while True:
        result, remainder = divmod (n, 2)
        converted_n += str(remainder)
        if result == 0:
            break
        n = result
    return "".join(list(reversed(converted_n)))

print(convert_dec_to_bin(2))
