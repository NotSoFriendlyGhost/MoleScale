from tkinter import *
import tkinter.messagebox as tmsg
from elements import *
import serial
import os
import subprocess

totalMolarMass = 0
weight = 0
keyboard_process = None

ser = serial.Serial("/dev/ttyACM0",  9600)

def add():
    entered_text = textentry.get()  # this will collect the text from the text entry box
    entered_amount = amountentry.get()
    try:
        results = entered_amount + ' x ' + elements[entered_text] + '\n'
    except Exception as e:
        tmsg.showerror("Error Occurred", "Please enter a valid element")
        return
    global totalMolarMass
    totalMolarMass += molar_masses[entered_text] * float(entered_amount)
    output.insert(END, results)

def displayWeight():
    weightoutput.delete(1.0, END)
    global totalMolarMass
    global weight
    weight = float(ser.readline())
    if totalMolarMass > 0:
        weightoutput.insert(END, abs(round(weight / totalMolarMass, 3)))
    else:
        weightoutput.insert(END, 'Enter an element to get started')
    root.after(250, displayWeight)

def reset():
    output.delete(1.0, END)
    global totalMolarMass
    totalMolarMass = 0

def tare():
    ser.write(b'T')

def toggle_keyboard():
    global keyboard_process
    if keyboard_process is None:
        keyboard_process = subprocess.Popen(["onboard"])
    else:
        keyboard_process.terminate()
        keyboard_process = None

def exit(event):
    root.destroy()

# main:
root = Tk()
root.geometry("800x480")
root.minsize(800, 480)
root.maxsize(1920, 1080)
root.title("Periodic Elements")
root.attributes('-zoomed', True)
root.bind("<Escape>", exit)

f1 = Frame(root, relief=SUNKEN)
f1.grid(row=0, column=0, columnspan=4, sticky='ew')
labl = Label(f1, text="Mole Scale", font="hack 12 bold").pack(padx=10, pady=5)

# create label
lab = Label(root, text='Enter an Element, Symbol or Atomic number:', font="Consolas 12 bold")
lab.grid(row=1, column=0, columnspan=4, sticky='w', padx=10, pady=2)

# create a text entry box
textentry = Entry(root, width=30, borderwidth=5, font="firacode 12", fg="#000000")
textentry.grid(row=2, column=0, columnspan=4, padx=10, pady=2, ipady=2, ipadx=2, sticky='ew')

# create label
lab = Label(root, text='Enter the Amount of this Element:', font="Consolas 12 bold")
lab.grid(row=3, column=0, columnspan=4, sticky='w', padx=10, pady=2)

# create a text entry box
amountentry = Entry(root, width=30, borderwidth=5, font="firacode 12", fg="#000000")
amountentry.grid(row=4, column=0, columnspan=4, padx=10, pady=2, ipady=2, ipadx=2, sticky='ew')

# add buttons
Button(root, text="ADD", font="Comicsansms 12", width=9, command=add).grid(row=5, column=0, padx=10, pady=2, sticky='w')
Button(root, text="RESET", font="Comicsansms 12", width=9, command=reset).grid(row=5, column=1, padx=10, pady=2, sticky='w')
Button(root, text="TARE", font="Comicsansms 12", width=9, command=tare).grid(row=5, column=2, padx=10, pady=2, sticky='e')
Button(root, text="Toggle Keyboard", font="Comicsansms 12", width=15, command=toggle_keyboard).grid(row=5, column=3, padx=10, pady=2, sticky='e')

# create another label
Label(root, text="Current Molecule:", font="Helvetica 12").grid(row=6, column=0, columnspan=4, sticky='w', padx=10, pady=2)

# create a text box
output = Text(root, width=75, height=6, wrap=WORD, background="#DAF7A6", font="Firacode 12")
output.grid(row=7, column=0, columnspan=4, padx=10, pady=2, sticky='ew')

# display weight
Label(root, text="Weight in Moles:", font="Helvetica 12").grid(row=8, column=0, columnspan=4, sticky='w', padx=10, pady=2)

weightoutput = Text(root, width=75, height=1, wrap=WORD, background="#DAF7A6", font="Firacode 12")
weightoutput.grid(row=9, column=0, columnspan=4, padx=10, pady=2, sticky='ew')

displayWeight()
root.mainloop()

