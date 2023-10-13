from string import ascii_uppercase as alphabet


def split_by_n (row, n):
    split_list = []
    s = ""
    for char in row:
        if len (s) == n:
            split_list.append (s)
            s = ""
        s += char
    return split_list


def get_font ():
    with open ("AsciiArtFont.txt", "r") as file:
        file_content = file.read ()
        rows = file_content.split ("\n")
        font_dic = {}
        for row in rows:
            split_row = split_by_n (row, 4)
            for i in range (len (split_row)):
                letter = alphabet [i]
                chars = split_row [i]
                if letter not in font_dic:
                    font_dic [letter] = [chars]
                else:
                    font_dic [letter].append (chars)
        file.close ()
        return font_dic


def print_with_font (text):
    text = text.upper ()
    font_dic = get_font()
    for i in range (6):
        for letter_index, letter in enumerate(text):
            separator = " "
            if letter in alphabet:
                letter_chars = font_dic [letter]
                current_letter_char = letter_chars [i]
                print (current_letter_char, end = separator)
            else:
                print (letter, end = separator)
        print ()


if __name__ == "__main__":
    print_with_font ("Hello World!")