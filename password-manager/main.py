import tkinter as tk
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, tk.END)
    password_input.insert(0, password)
    pyperclip.copy(password)
    # print(f"Your password is: {password}, length = {len(password)}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if website == "" or password == "" or email == "":
        messagebox.showwarning(title="You forgot something", message="Don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: "
                                                              f"\nWebsite: {website} \nEmail: {email} \nPassword: {password}")
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password}\n")
            website_input.delete(0, tk.END)
            # email_input.delete(0, tk.END)
            password_input.delete(0, tk.END)
            website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("PP Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200)
lock_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = tk.Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = tk.Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = tk.Label(text="Password:")
password_label.grid(column=0, row=3)

website_input = tk.Entry(width=36)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

email_input = tk.Entry(width=36)
email_input.insert(0, "william@email.com")
email_input.grid(column=1, row=2, columnspan=2)

password_input = tk.Entry(width=18)
password_input.grid(column=1, row=3)

generate_button = tk.Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=31, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
