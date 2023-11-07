# en cas de hex, convertir en dec, puis en bin
# en cas de dec, convertir en bin directement


# importation fonc de Marc Antoine, pour convertir tout n \
# ayant une base définit en binaire, necessaire pour convertir de hex en bin
from ConvertToDec import convert_to_dec


# renverser la chaîne de caractères
def reverse_str (t):
    return t [::-1]


# convertir du decimal au binaire, renversement du résultat pour l'afficher correctement
def convert_dec_to_bin (n):
    converted_n = ""

    while True:
        result, remainder = divmod (int (n), 2)
        converted_n += str (remainder)
        if result == 0:
            break
        n = result

    converted_n = reverse_str (converted_n)
    return converted_n


# utilisation de la fonction convert_to_dec, obtention du résultat en dec, puis conversion en bin, via la fonction édictée plus haut
def convert_hex_to_bin (h):
    n = int (convert_to_dec (h, "hex"))
    return convert_dec_to_bin (n)


# choix des fonctions utilisées pour convertir 'n' en base binaire
def convert_to_bin (n, base):
    if base == "dec":
        return convert_dec_to_bin(n)
    elif base == "hex":
        return convert_hex_to_bin(n)
    elif base == "bin":
        return n
    else:
        return "vous n'avez pas entrer une base correcte, veuillez rééssayer avec une hex, bin ou dec"


if __name__ == "__main__":
	print(convert_to_bin("-1988971", "dec") == "-111100101100101101011")
	print(convert_to_bin("1ae867f987d", "hex") == "11010111010000110011111111001100001111101")
	print(convert_to_bin("100100101", "bin") == "100100101")
