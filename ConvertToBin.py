# en cas de hex, convertir en dec, puis en bin
# en cas de dec, convertir en bin directement

from ConvertToDec import convert_to_dec
# importation fonc de Marc Antoine, pour convertir tout n \
# ayant une base définit en binaire, necessaire pour convertir de hex en bin

def convert_dec_to_bin (n):
    converted_n = ""
    while True:
        result, remainder = divmod (int (n), 2)
        converted_n += str(remainder)
        if result == 0:
            break
        n = result
    return "".join(list(reversed(converted_n)))
# convertir du decimal au binaire, renversement du resultat pour l'afficher correctement

def convert_hex_to_bin (n):
    n = convert_to_dec(n, "hex")
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
    return convert_to_bin
#choix des fonctions utilisés pour convertir n en base bin




print(convert_to_bin("1988971", "dec"))
print(convert_to_bin("1ae867f987d", "hex"))
print(convert_to_bin("100100101", "bin"))
