from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=30)


def output_kms():
    miles = int(entry.get())
    kms = round(miles * 1.609)
    km_output.config(text=kms)


entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(column=1, row=0)

label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_is_equal = Label(text="is equal to")
label_is_equal.grid(column=0, row=1)

km_output = Label(text="0")
km_output.grid(column=1, row=1)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

calculate = Button(text="Calculate", command=output_kms)
calculate.grid(column=1, row=2)

window.mainloop()


