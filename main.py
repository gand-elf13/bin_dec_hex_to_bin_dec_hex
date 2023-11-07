from ParseInput import get_inputs, output_result, wait_for_input
from AsciiArt import print_with_font


'''
introduce_program is a function that simply prints a description about the program.
It takes no arguments, and returns None.
This function is executed before the program starts.
'''
def introduce_program ():
    print_with_font ("BIN-DEC-HEX")
    print ("This is a program, made by GALTIER Maxime & DUCLOS Marc-Antoine & RACIC Leonardo, " \
        + "able to convert numbers into different supported bases (binary, decimal, and hexadecimal currently).")
    print ("After finishing converting, this program will display all the realised conversions, and will update conversions.txt")
    print ("If you want to quit the program at any point of the algorithm, input 'EXIT'.")
    print ("[[[Do keep in mind that if you do input 'EXIT', all the current conversions won't be saved in results.txt!]]]")
    print ("Please keep in mind that the program is case sensitive!")
    print ("(Hexadecimals' letters are input and output in lowercase!)")


'''
get_str_list_conversions is a function taking a list containing dictionaries (conversions) and
returns a list containing a text summarising each conversions dictionary. As such,
it returns a list of string, whilst taking a list of dictionaries as a parameter.
'''
def get_str_list_conversions (conversions):
    str_list_conversions = []
    for c in conversions:
        text = "(" + c ["initial_base"] + ")  " + c ["n"] + "  ==>  " \
            + c ["conversion_result"] + "  (" + c ["final_base"] + ")"
        str_list_conversions.append (text)
    return str_list_conversions


'''
update_txt_file is a function taking a list containing dictionaries (conversions) and
saves all conversions done whilst using the program, unless the user decided to exit mid-process...
It returns None subsequently
'''
def update_txt_file (conversions):
    with open ("conversions.txt", "a") as file:
        conversions_texts = get_str_list_conversions (conversions)
        file.write ("\n".join (conversions_texts) + "\n")
        file.close ()
    print ("The realised conversions are successfully " \
        + "appended into the conversions.txt file in the repository.")


'''
display_conversions is a function that takes a list of conversions (a list of dictionaries)
and outputs them. As such, it takes only one argument (conversions) and returns none
'''
def display_conversions (conversions):
    print ("These are all the conversions you have done until now : ")
    for text in get_str_list_conversions (conversions):
        print (text)


'''
MAIN PART OF THE PROGRAM
'''
if __name__ == "__main__":
    introduce_program ()
    conversions = []

    while True:
        n, initial_base, final_base = get_inputs ()

        conversion_result = output_result (n, initial_base, final_base)
        conversion_dict = {
            "n" : n,
            "initial_base" : initial_base,
            "final_base" : final_base,
            "conversion_result" : conversion_result,
        }
        conversions.append (conversion_dict)

        print ("\n")
        should_continue = wait_for_input (
            "Do you want the program to convert another number? (y/n) : ",
            "ERROR : IT IS A YES OR NO QUESTION (WRITE IN LOWERCASE)",
            "y", "n",
        )
        if should_continue == "n":
            display_conversions (conversions)
            update_txt_file (conversions)
            print ("PROCESS IS NOW EXITING - THE CONVERSIONS WON'T BE SAVED")
            break
        else:
            print ("\n")
