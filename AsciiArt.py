from string import ascii_uppercase as alphabet


'''
get_font is a function that reads the font.txt file and returns a dictionary
containing the font to apply (it takes no parameters)
'''
def get_font ():
    with open ("font.txt", "r") as file:
        file_content = file.read ()
        rows = file_content.split ("\n")
        font_dic = {}

        for j in range (26):
            letter = alphabet [j]
            list_character = []
            for i in range (8):
                list_character.append (rows [j * 8 + i])
            
            font_dic [letter] = list_character

        file.close ()

        return font_dic
    

'''
print_with_font is a function that prints a string
in a certain font contained in a dictionary that is returned by
the get_font function.
It takes one argument : text (string)
It returns None.
'''
def print_with_font (text):
    text = text.upper ()
    font_dic = get_font ()
    for i in range (8):
        for letter_index, letter in enumerate (text):
            separator = " "
            if letter in alphabet:
                letter_chars = font_dic [letter]
                current_letter_char = letter_chars [i]
                print (current_letter_char, end = separator)
            else:
                print (letter, end = separator)
        print()


if __name__ == "__main__":
    print_with_font ("test")
