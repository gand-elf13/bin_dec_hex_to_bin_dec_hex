# en cas de hex, convertir en dec, puis en bin
# en cas de dec, convertir en bin directement

from ConvertToDec import convert_to_dec
# importation fonc de Marc Antoine, pour convertir tout n \
# ayant une base définit en binaire, necessaire pour convertir de hex en bin


def reverse_str (t):
    return t [::-1]


def convert_dec_to_bin (n):
    converted_n = ""
    is_negative = int (n) < 0
    if is_negative:
        n = n [1:]
    while True:
        result, remainder = divmod (int (n), 2)
        converted_n += str(remainder)
        if result == 0:
            break
        n = result
    converted_n = reverse_str (converted_n)
    if is_negative:
        converted_n = "-" + converted_n
    return converted_n
# convertir du decimal au binaire, renversement du resultat pour l'afficher correctement

def convert_hex_to_bin (n):
    n = int(convert_to_dec(n, "hex"))
    return convert_dec_to_bin(n)
# utilisation d'la fonc de M-A, puis resultat obtenu en dec converti en bin via la fonction édictée plus haut

def convert_to_bin (n, base):
    if base == "dec":
        return convert_dec_to_bin(n)
    elif base == "hex":
        return convert_hex_to_bin(n)
    elif base == "bin":
        return n
    else:
        return "vous n'avez pas entrer une base correcte, veuillez rééssayer avec une hex, bin ou dec"
#choix des fonctions utilisés pour convertir n en base bin



if __name__ == "__main__":
	print(convert_to_bin("-1988971", "dec") == "-111100101100101101011")
	print(convert_to_bin("1ae867f987d", "hex") == "11010111010000110011111111001100001111101")
	print(convert_to_bin("100100101", "bin") == "100100101")
