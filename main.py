from ParseInput import get_inputs, output_result, wait_for_input
from AsciiArt import print_with_font


'''
introduce_program is a function that simply prints a description about the program.
It takes no arguments, and returns None.
This function is executed before the program starts.
'''
def introduce_program ():
    print_with_font ("BDH-TO-BDH")
    print ("This is a program, made by GALTIER Maxime & DUCLOS Marc-Antoine & RACIC Leonardo, " \
        + "able to convert numbers into different supported bases (binary, decimal, and hexadecimal currently).")
    print ("If you want to quit the program at any point of the algorithm, input 'EXIT'.")
    print ("Please keep in mind that the program is case sensitive!")
    print ("(Hexadecimals' letters are input and output in lowercase!)") 


'''
display_conversions is a function that takes a list of conversions (a list of dictionaries)
and outputs them. As such, it takes only one argument (conversions) and returns none
'''
def display_conversions (conversions):
    print ("These are all the conversions you have done until now : ")
    for c in conversions:
        text = "(" + c ["initial_base"] + ")  " + c ["n"] + "  ==>  " \
            + c ["conversion_result"] + "  (" + c ["final_base"] + ")" 
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
            "ERROR : IT IS A YES OR NO QUESTION ",
            "y", "n",
        )
        if should_continue == "n":
            display_conversions (conversions)
            print ("PROCESS IS NOW EXITING")
            break
        else:
            print ("\n")
