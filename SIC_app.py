"""
Project: A GUI Program to calculate Simple Interest given Principal, Rate and Time.
Date: 27/08/2022
Author: David

"""

from tkinter import *

root = Tk()
root.title("Simple Interest Calculator")
root.geometry("500x300+800+50")
root.resizable(0, 0)


# Define the functions
def Calculate():
    principal = int(principal_entry.get())  # equivalent of principal = int(input("Principal"))
    rate = int(rate_entry.get())
    time = int(time_entry.get())
    interest = (principal * rate * time) / 100
    Label(text=f"Interest\n{round(interest, 2)}", font="arial 25 bold").place(x=350, y=90)


def Reset():
    principal_entry.delete(0, 'end')
    rate_entry.delete(0, 'end')
    time_entry.delete(0, 'end')


# Define the labels widgets
principal = Label(root, text="Principal", font=('arial', 15)).place(x=50, y=20)
# principal.pack(x=50, y=20) #places labels on the screen
rate = Label(root, text="Rate of Interest", font=('arial', 15)).place(x=50, y=90)
time = Label(root, text="Time(years)", font=('arial', 15)).place(x=50, y=160)

# Define the interest label
interest = Label(root, text="Interest:", font="arial 15").place(x=350, y=20)

principalvalue = StringVar()
ratevalue = StringVar()
timevalue = StringVar()

# Define the Entries widgets
principal_entry = Entry(root, textvariable=principalvalue, font="arial 20", width=8)
principal_entry.place(x=200, y=20)
rate_entry = Entry(root, textvariable=ratevalue, font="arial 20", width=8)
rate_entry.place(x=200, y=90)
time_entry = Entry(root, textvariable=timevalue, font="arial 20", width=8)
time_entry.place(x=200, y=160)

# Define the Button widgets
Button(root, text="Calculate", font="arial 15", command=Calculate).place(x=50, y=220)
Button(root, text="Reset", font="arial 15", command=Reset).place(x=200, y=220)
Button(root, text="Exit", command=lambda: exit(), font="arial 15", width=8).place(x=350, y=220)

root.mainloop()