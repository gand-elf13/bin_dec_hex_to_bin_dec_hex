import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("BDH--converter")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_483=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_483["font"] = ft
        GLabel_483["fg"] = "#333333"
        GLabel_483["justify"] = "center"
        GLabel_483["text"] = "THE BDH CONVERTER"
        GLabel_483.place(x=160,y=80,width=247,height=57)

        GLineEdit_971=tk.Entry(root)
        GLineEdit_971["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_971["font"] = ft
        GLineEdit_971["fg"] = "#333333"
        GLineEdit_971["justify"] = "center"
        GLineEdit_971["text"] = "to convert"
        GLineEdit_971.place(x=220,y=190,width=70,height=25)

        GButton_509=tk.Button(root)
        GButton_509["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_509["font"] = ft
        GButton_509["fg"] = "#000000"
        GButton_509["justify"] = "center"
        GButton_509["text"] = "Claculate"
        GButton_509["relief"] = "raised"
        GButton_509.place(x=220,y=350,width=70,height=25)
        GButton_509["command"] = self.GButton_509_command

        GButton_642=tk.Button(root)
        GButton_642["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_642["font"] = ft
        GButton_642["fg"] = "#000000"
        GButton_642["justify"] = "center"
        GButton_642["text"] = "Binary"
        GButton_642.place(x=130,y=240,width=70,height=25)
        GButton_642["command"] = self.GButton_642_command

        GButton_140=tk.Button(root)
        GButton_140["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_140["font"] = ft
        GButton_140["fg"] = "#000000"
        GButton_140["justify"] = "center"
        GButton_140["text"] = "Decimal"
        GButton_140.place(x=130,y=280,width=70,height=25)
        GButton_140["command"] = self.GButton_140_command

        GButton_404=tk.Button(root)
        GButton_404["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_404["font"] = ft
        GButton_404["fg"] = "#000000"
        GButton_404["justify"] = "center"
        GButton_404["text"] = "Hexadecimal"
        GButton_404.place(x=130,y=320,width=70,height=25)
        GButton_404["command"] = self.GButton_404_command

        GLabel_450=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_450["font"] = ft
        GLabel_450["fg"] = "#333333"
        GLabel_450["justify"] = "center"
        GLabel_450["text"] = "from :"
        GLabel_450.place(x=130,y=190,width=70,height=25)

        GLabel_231=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_231["font"] = ft
        GLabel_231["fg"] = "#333333"
        GLabel_231["justify"] = "center"
        GLabel_231["text"] = "to :"
        GLabel_231.place(x=310,y=190,width=70,height=25)

        GButton_579=tk.Button(root)
        GButton_579["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_579["font"] = ft
        GButton_579["fg"] = "#000000"
        GButton_579["justify"] = "center"
        GButton_579["text"] = "Binary"
        GButton_579.place(x=310,y=240,width=70,height=25)
        GButton_579["command"] = self.GButton_579_command

        GButton_132=tk.Button(root)
        GButton_132["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_132["font"] = ft
        GButton_132["fg"] = "#000000"
        GButton_132["justify"] = "center"
        GButton_132["text"] = "Decimal"
        GButton_132.place(x=310,y=280,width=70,height=25)
        GButton_132["command"] = self.GButton_132_command

        GButton_155=tk.Button(root)
        GButton_155["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_155["font"] = ft
        GButton_155["fg"] = "#000000"
        GButton_155["justify"] = "center"
        GButton_155["text"] = "Hexadecimal"
        GButton_155.place(x=310,y=320,width=70,height=25)
        GButton_155["command"] = self.GButton_155_command

        GMessage_693=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_693["font"] = ft
        GMessage_693["fg"] = "#333333"
        GMessage_693["justify"] = "center"
        GMessage_693["text"] = "Message"
        GMessage_693.place(x=220,y=400,width=80,height=25)

    def GButton_509_command(self):
        print("command")


    def GButton_642_command(self):
        ConvertFrom = bin


    def GButton_140_command(self):
        ConvertFrom = dec


    def GButton_404_command(self):
        ConvertFrom = hex


    def GButton_579_command(self):
        ConvertTo = bin


    def GButton_132_command(self):
        ConvertTo = dec


    def GButton_155_command(self):
        ConvertTo = hex

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
