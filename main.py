from ParseInput import get_inputs, output_result, wait_for_input

'''
introduce_program is a function that simply prints a description about the program.
It takes no arguments, and returns None.
This function is executed before the program starts.
'''
def introduce_program ():
    print ("This is a program used to convert numbers into different bases")
    print ("Please keep in mind that the program is case sensitive!")


'''
MAIN PART OF THE PROGRAM
'''
if __name__ == "__main__":
    introduce_program ()
    while True:
        n, initial_base, final_base = get_inputs ()
        output_result (n, initial_base, final_base)
        print ("\n")
        should_continue = wait_for_input (
            "Do you want the program to convert another number? (y/n) : ",
            "ERROR : IT IS A YES OR NO QUESTION ",
            "y", "n",
        )
        if should_continue == "n":
            print ("PROCESS IS NOW EXITING")
            break
		else:
	    	print ("\n")
