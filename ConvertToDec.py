
#cette fonction convertis les lettres des chaines hexadecimales en leur valeure corespondante
#prend en input un caractere de la chaine a convertir et return sa valeur correspondante.

def convert_str_to_int (remainder):

    #dictionnaire des lettres et de leur valeur correspondante.
    higher_coefs = {"a":10,"b":11,"c":12,"d":13,"e":14,"f":15 }

    #verifie si l'input est une lettre
    if remainder not in higher_coefs:
        
        #si l'input n'est pas une letttre, on renvoie la valeur d'entree.
        return str (remainder)
    else:

        #si l'input est une lettre presente dans le dictionnaire, on renvoie la valeur correspondate.
        return higher_coefs [remainder]



#cette fonction convertis une chaine hexadecimale en decimal.
#elle prend en entree une chaine de caractére et retourne un entier.
def convert_hex_to_dec(n):

    #transforme l'input en chaine de caractere pour eviter les cas extremes.
    n = str(n)
    #definis les variables; converted_n : la chaine convertis qui sera retournée , power : la puissance 
    converted_n = 0
    power = 0

    #boucle principale de la fonction, on utilise reversed() pour passer dans la chaine de droite a gauche
    for i in reversed(n):
        
        #ajoute a converted_n la valeur convertie de l'element de la chaine (i), multipliée par : 
        # 16 a la puissane power qui correspond a la place de l'element dans la chaine de caractere.
        converted_n += int(convert_str_to_int(i))*(16**power)

        #ajoute 1 a la puissance de la fonction ci dessus car on passe a l'element suivant
        power += 1
    #retourne l'entier convertis.
    return str(converted_n)

#cette fonction convertis un binaire en decimal,
#elle prend en entree un binaire qui peut etre sous forme d'un entier ou d'une chaine de caractere.
def convert_bin_to_dec(n):
    
    #transforme l'input en chaine de caractere pour eviter les cas extremes.
    n = str(n)

    #definis les variables; converted_n : la chaine convertis qui sera retournée , power : la puissance 
    converted_n = 0
    power = 0

    #boucle principale de la fonction, on utilise reversed() pour passer dans la chaine de droite a gauche
    for i in reversed(n):
        
        #ajoute a converted_n la valeur convertie de l'element de la chaine (i), multipliée par : 
        # 16 a la puissane power qui correspond a la place de l'element dans la chaine de caractere.
        converted_n += int(i)*(2**power)

        #ajoute 1 a la puissance de la fonction ci dessus car on passe a l'element suivant
        power += 1

    #retourne l'entier convertis.
    return str(converted_n)

#cette fonction convertis une chaine decimale, binaire ou hexadecimale en decimal.
#prend en entree une chaine et la base de cette chaine, retourne la chaine equivalente en decimal.
def convert_to_dec(n,base):
    
    answ = 0

    #si la base est reconnue, renvoie le resultat de la fonction correspondante,
    #si la base est decimal renvoie l'entree si la base est inconnjue renvoie une erreur
    if base == "bin":
        answ = convert_bin_to_dec(n)
    elif base == "dec":
        answ = n
    elif base == "hex":
        answ = convert_hex_to_dec(n)
    else:
        print("ERROR BASE NOT SUPORTED YET")
        answ = "ERROR BASE NOT SUPORTED YET"

    return answ

if __name__ == "__main__":
	print(convert_to_dec("1988971", "dec") == "1988971")
	print(convert_to_dec("1e596b", "hex") == "1988971")
	print(convert_to_dec("111100101100101101011", "bin") == "1988971")
