# Documentation
---
## Organisation des fichiers

Les conversions sont effectuées par 3 fichiers : 
- [ConvertToBin.py](../ConvertToBin.py)
- [ConvertToDec.py](../ConvertToDec.py)
- [ConvertToHex.py](../ConvertToHex.py)

L'IHM est assurée par le fichier :
- [ParseInput.py](../ParseInput.py)

Utilisant les fichiers :

- [AsciiArt.py](../AsciiArt.py)
- [AsciiArtFont.txt](../AsciiArtFont.txt)

Afin de générer le titre.

La mise en relation des différentes parties du programme est effectuée par le fichier :

- [main.py](../main.py)

## Les principales fonctions:

### Dans ConvertToDec.py

- `convert_to_dec (n, base)` est une fonction qui transforme n'importe quelle chaîne de caractères `n` associée à une base disponible appelée `base` en un nombre décimal.
Cette fonction utilise les fonctions :

- `convert_hex_to_dec (b)` convertissant un hexadecimal `b` en décimal

- `convert_bin_to_dec (b)` convertissant un binaire `b` en décimal

### Dans ConvertToHex.py

- `convert_to_hex (n, base)` transformant n'importe quelle chaîne de caractères `n` associée à une base disponible appelée `base` en un nombre hexadécimal.
elle utilise les fonctions :

- `convert_dec_to_hex (b)` convertissant un décimal `b` en hexadécimal

- `convert_bin_to_hex (b)` convertissant un binaire `b` en un hexadécimal, en le convertissant d'abord en décimal via `convert_to_dec` puis en hexadécimal via `convert_dec_to_hex`.

### Dans ConvertToBin.py

- `convert_to_bin (n, base)` transformant n'importe quelle chaîne de caractères `n` associée a une base disponible appelée `base` en un nombre binaire.
elle utilise les fonctions :

- `convert_dec_to_bin (b)` convertissant un décimal `b` en binaire

- `convert_hex_to_bin (b)` convertissant un hexadécimal `b` en un binaire, en le convertissant d'abord en décimal via `convert_to_dec` puis en binaire via `convert_dec_to_bin`.

### Dans ParseInput

- `output_result (n, initial_base, final_base)` est une fonction affichant le résultat de la conversion de l'entier naturel `n` en base `initial_base` à la base `final_base`. Cette fonction prend en arguments trois strings et ne retourne rien.

- `get_inputs ()` est une fonction permettant de recueillir les entrées de l'utilisateur (étant le nombre entier à convertir, sa base, ainsi que la base dans laquelle on veut convertir l'entier naturel). Par conséquence, cette fonction ne prend aucun argument, mais renvoie trois strings.

- `wait_for_input (text, error_text, *possible_inputs)` est une fonction permettant d'obtenir une entrée de l'utilisateur après avoir afficher le string `texte`. Si l'entrée donnée n'est pas dans les différents `*possible_inputs`, alors on affiche `error_text` et on redemande à l'utilisateur d'entrer une information jusqu'à ce qu'elle soit validée.

### Dans AsciiArt

- `print_with_font (text)` est une fonction qui premierement importe l'equivalent de chaque lettre a l'aide de la fonction `get_font`. elle utilise ces equivqlence pour ecrire un texte donné en argument avec la police choisie.

- `get_font ()` est une fonction qui retourne un dictionnaire comprenant pour chaque lettre une liste correspondant a chaque ligne de la police.

### Dans main

- `introduce_program ()` ecrit les informations d'utilisation du programme ainsi que le titre a l'aide de la fonction `print_with_font ()` importée depuis [AsciiArt.py](../AsciiArt.py)

## Utilisation

Chaque fichier peut être utilisé indépendemment des autres, mis à part ConvertToBin.py et ConvertToHex.py qui emploient ConvertToDec, en l'important a l'aide du keyword `import`.
