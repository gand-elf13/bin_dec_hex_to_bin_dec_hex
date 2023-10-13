# Documentation

## Organisation des fichiers.

les conversions sont effectuées par 3 fichiers : 
- [ConvertToBin.py](../ConvertToBin.py)
- [ConvertToDec.py](../ConvertToDec.py)
- [ConvertToHex.py](../ConvertToHex.py)

l'IHM est assurée par le fichier :
- [ParseInputs.py](../ParseInput.py)

qui utilise les fichiers :

- [AsciiArt.py](../AsciiArt.py)
- [AsciiArtFont.py](../AsciiArtFont.txt)

afin de generer le titre.

la mise en relation des differentes parties du programme est effectue par le fichier :

- [main.py](../main.py)

## les fonctions:

### Dans Convert To Dec

la fonction :  `convert_to_dec (n, base)`

transforme n'importe quelle chaine de charactere `n` associée a une base suportée `base` en un nombre decimal.
elle utilise les fonctions :

- `convert_hex_to_dec (b)`

qui convertis un hexadecimal `b` en decimal

- `convert_bin_to_dec (b)`

qui convertis un binaire `b` en un decimal

### Dans Convert To Hex

la fonction :  `convert_to_hex (n, base)`

transforme n'importe quelle chaine de charactere `n` associée a une base suportée `base` en un nombre hexadecimal.
elle utilise les fonctions :

- `convert_dec_to_hex (b)`

qui convertis un decimal `b` en hexadecimal

- `convert_bin_to_hex (b)`

qui convertis un binaire `b` en un hexadecimal. en le convertissant en decimal avec `convert_to_dec` puis en hexadecimal en utilisant la fonction `convert_dec_to_hex()`.

### Dans Convert To Bin

la fonction :  `convert_to_bin (n, base)`

transforme n'importe quelle chaine de charactere `n` associée a une base suportée `base` en un nombre binaire.
elle utilise les fonctions :

- `convert_dec_to_bin (b)`

qui convertis un decimal `b` en binaire

- `convert_hex_to_bin (b)`

qui convertis un hexadecimal `b` en un binaire. en le convertissant en decimal avec `convert_to_dec` puis en binaire en utilisant la fonction `convert_dec_to_bin()`.

### Dans ParseInput

WIP


### Dans AsciiArt

WIP

### Dans main

WIP

## Utilisation

Chaque fichier peut etre utilise independament des autre a part ConvertToBin et ConvertToHex qui utilisent ConvertToDec, en l'important a l'aide de la fonction `import`.
