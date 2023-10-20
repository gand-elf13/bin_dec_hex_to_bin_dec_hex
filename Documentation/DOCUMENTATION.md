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

WIP


### Dans AsciiArt

WIP

### Dans main

WIP

## Utilisation

Chaque fichier peut être utilisé indépendemment des autres, mis à part ConvertToBin.py et ConvertToHex.py qui emploient ConvertToDec, en l'important a l'aide du keyword `import`.
