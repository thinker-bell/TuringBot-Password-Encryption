from tkinter import filedialog
from tkinter import*
import math, sys, numpy as np
from numpy.fft import fft
import random
import os


#======================================================================

root = Tk()
Tk().withdraw()
root.geometry("500x400")
root.title("Password Program")

#================Variable Declaration=================================
keyAB = StringVar()
keyC = DoubleVar()
folder_path_textfile = StringVar()
status_text = StringVar()
inputP = StringVar()

keyC = np.random.rand(1,1)*10**(np.round(np.random.rand(1,1)*6))
#================Window Framing=================================
window = Frame(root, width = 1000, relief = SUNKEN)
window.pack(side=TOP)

#=========================Info========================================
lblInfo = Label(window, font=('arial', 15, 'bold'),  text="\nThe Decryption Program",fg="Black")
lblInfo.grid(row=0,column=0)

lblInfo = Label(window, font=('arial', 10, 'bold'), text=" \n\n Please enter your weak password: ", fg="Black")
lblInfo.grid(row=3,column=0)

lblInfo = Label(window, font=('arial', 10, 'bold'), text="\n\n Please see below your encrypted password: ", fg="Black")
lblInfo.grid(row=7,column=0)

lblInfo = Label(window, font=('arial', 10, 'bold'), text=" \n\n Below is the file path where your password is saved: ", fg="Black")
lblInfo.grid(row=14,column=0)

#=========================Operation========================================
def browse_button_textfile():
    file_path=filedialog.askopenfilename()
    folder_path_textfile.set(file_path)
    print (folder_path_textfile)


def generate_password():



    #===========================File Save=================================
    file_path = (os.getcwd()+"\password.txt")

    #Open file and write result.
    with open(file_path, "w") as file:
        file.write(password)

    #State where file has been saved.
    status_text.set(os.path.abspath("password.txt"))
    #print("Password saved to:", file_path)

    return password #Return the result



#=========================Display========================================
txtDisplay = Entry(window, font=('arial',10),  textvariable=inputP, bd=5,width =50, bg="white")
txtDisplay.grid(row=4,column=0)


txtDisplay = Entry(window, font=('arial',10), textvariable=keyAB, bd=5, width =50, bg="white")
txtDisplay.grid(row=8,column=0)

txtDisplay = Entry(window, font=('arial',10), textvariable=status_text, bd=5, width =50, bg="white")
txtDisplay.grid(row=15,column=0)

#=========================Button========================================
btnbrowsetxt=Button(window, padx=5,pady=5,bd=5,fg="black", font=('arial', 10,'bold'), text="Find the hidden Password",
            bg ="pink",  command =generate_password).grid(row=5,column=0)

#btnstep4=Button(window, padx=5,pady=5,bd=5,fg="black", font=('arial', 10,'bold'), text="Decrypt Message",
 #           bg ="pink", command =decryptButton).grid(row=12,column=0)

# def on_closing():
#     quit()

# root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()