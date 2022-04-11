from tkinter import *


def convert():
    miles = float(miles_entry.get())
    km = round(miles * 1.60934, 1)
    km_label_c['text'] = km


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=30, pady=30)

miles_entry = Entry(width=15)
miles_entry.grid(column=2, row=1)
miles_entry.insert(END, string="0")

miles_label = Label(text="Miles")
miles_label.grid(column=3, row=1)

km_label_l = Label(text="is equal to")
km_label_l.grid(column=1, row=2)

km_label_c = Label(text="0")
km_label_c.grid(column=2, row=2)

km_label_r = Label(text="km")
km_label_r.grid(column=3, row=2)

calculate_button = Button(text="Calculate", command=convert)
calculate_button.grid(column=2, row=3)


window.mainloop()
