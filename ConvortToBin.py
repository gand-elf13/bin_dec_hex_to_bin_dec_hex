# convertir dec en entier, puis en bin

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
