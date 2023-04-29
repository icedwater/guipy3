#! /usr/bin/env python3

"""
Creating a basic Python GUI app to showcase tkinter/ttkBootstrap.
"""

import tkinter as tk
from tkinter import ttk

# reusable settings
HEADER_FONT = "Arial 30"
DEFAULT_FONT = "Calibri 15"


def clear_all():
    celsius_box.delete(0, tk.END)
    fahrenheit_box.delete(0, tk.END)

def convertCtoF():
    try:
        fahrenheit.set(str(int(celsius.get()) * (9 / 5) + 32))
        print(f"From {celsius}°C: {fahrenheit}°F.")
    except ValueError:
        status_msg.set(f"{celsius.get()} is not a valid number.")

def convertFtoC():
    try:
        celsius.set(str((int(fahrenheit.get()) - 32) * (5 / 9)))
        print(f"From {fahrenheit}°F: {celsius}°C.")
    except ValueError:
        status_msg.set(f"{fahrenheit.get()} is not a valid number.")

def convert_temp():
    print(f"{celsius.get()}, {fahrenheit.get()}, {convert_to.get()}")
    if convert_to.get() == "C":
        convertFtoC()
    elif convert_to.get() == "F":
        convertCtoF()

# setup
window = tk.Tk()
window.title("Temperature Conversion")
window.geometry("500x250")

# header
header = tk.Label(master=window, text="Celsius or Fahrenheit", font=HEADER_FONT)
header.pack()

# two textboxes separated by a space
textbox_frame = tk.Frame(master=window)

celsius = tk.StringVar()
fahrenheit = tk.StringVar()

celsius_label = ttk.Label(
        master=textbox_frame,
        text="C",
        font=DEFAULT_FONT)
fahrenheit_label = ttk.Label(
        master=textbox_frame,
        text="F",
        font=DEFAULT_FONT)

celsius_box = tk.Entry(
        master=textbox_frame,
        textvariable=celsius,
        font=DEFAULT_FONT)

fahrenheit_box = tk.Entry(
        master=textbox_frame,
        textvariable=fahrenheit,
        font=DEFAULT_FONT)

celsius_label.pack(side=tk.LEFT)
celsius_box.pack(side=tk.LEFT)
fahrenheit_label.pack(side=tk.LEFT)
fahrenheit_box.pack(side=tk.LEFT)
textbox_frame.pack()

# radio button to decide convert direction
label_frame = tk.Frame(master=window)

convert_to = tk.StringVar()

c_to_f = tk.Radiobutton(
        master=label_frame,
        text="C to F",
        variable=convert_to,
        value="F")

f_to_c = tk.Radiobutton(
        master=label_frame,
        text="F to C",
        variable=convert_to,
        value="C")

c_to_f.pack(side=tk.LEFT)
f_to_c.pack(side=tk.LEFT)
label_frame.pack()

# buttons to update, clear, or quit
button_frame = tk.Frame(master=window)

update_button = tk.Button(
        master=button_frame,
        text="Update",
        command=convert_temp)

clear_button = tk.Button(
        master=button_frame,
        text="Clear",
        command=clear_all)

quit_button = tk.Button(
        master=button_frame,
        text="Quit",
        command=window.quit)

update_button.pack()
clear_button.pack()
quit_button.pack()
button_frame.pack()

# status bar
status_frame = tk.Frame(master=window)

status_msg = tk.StringVar()

status_bar = tk.Label(
        master=status_frame,
        textvariable=status_msg,
        relief=tk.SUNKEN)

status_bar.pack(fill=x)
status_frame.pack()

# run
window.mainloop()
