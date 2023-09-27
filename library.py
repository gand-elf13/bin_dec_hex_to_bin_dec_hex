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