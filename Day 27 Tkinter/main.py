import tkinter


def button_clicked():
    print("Hello WOrld")
    global times_clicked
    times_clicked += 2
    make_big = font_size + times_clicked
    my_label["text"] = input.get() # .get() to get whatever text is in the entry
    my_label["font"] = ('Arial', make_big, 'bold')


window = tkinter.Tk()
window.title("My first GUI")
window.minsize(width=600, height=600)
window.config(padx=20, pady=20)  # add padding/space around stuff

# Label
my_label = tkinter.Label(text="I am a label", font=('Arial', 24, 'bold'))
my_label["text"] = "ayy lmao"
my_label["foreground"] = "red"
my_label["background"] = "green"
font_size = 24
times_clicked = 0
# my_label.pack()  # used to layout components on the screen, can't be used with grid
# my_label.place(x=0, y=0)  # another way to place widgets, requires x and y coor
my_label.grid(column=0, row=0)

# Button 1

button = tkinter.Button(text="Hello world", command=button_clicked, padx=10, pady=10)
button.grid(column=2, row=2)

# Button 2

button_2 = tkinter.Button(text="New Button")
button_2.grid(column=3, row=1)

# Entry

input = tkinter.Entry()
input.grid(column=4, row=3)


window.mainloop()  # keeps the window open
