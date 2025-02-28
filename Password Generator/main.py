from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    final_password = "".join(password_list)
    pass_e.delete(0, END)
    pass_e.insert(0, final_password)
    pyperclip.copy(final_password)


# ------------------------------- Search ------------------------------------#
def search():
    website = web_e.get()
    try:
        with open("saved_passwords.json", mode="r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            messagebox.showinfo(title=f"{website}", message=f"Email: {data[website]["email"]}"
                                                            f"\nPassword: {data[website]["password"]}")
        else:
            messagebox.showinfo(title="Error", message="No details for the website")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_in_file():
    website = web_e.get()
    email = email_e.get()
    password = pass_e.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message=f"Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                              f"\nPassword: {password} \nIs ok to save?")
        if is_ok:
            try:
                with open("saved_passwords.json", mode="r") as f:
                    # Reading old data
                    data = json.load(f)
            except FileNotFoundError:
                with open("saved_passwords.json", mode="w") as f:
                    json.dump(new_data, f, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)

                with open("saved_passwords.json", mode="w") as f:
                    # Saving updated data
                    json.dump(data, f, indent=4)
            finally:
                web_e.delete(0, END)
                pass_e.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)
# Buttons
gen_b = Button(text="Generate Password", command=generate_password)
gen_b.grid(column=2, row=3, sticky=E)
add_b = Button(text="add", width=43, command=save_in_file)
add_b.grid(column=1, row=4, columnspan=2)
search_b = Button(text="Search", width=14, command=search)
search_b.grid(column=2, row=1, sticky=E)
# Entries
web_e = Entry(width=33)
web_e.grid(column=1, row=1)
web_e.focus()
email_e = Entry(width=51)
email_e.grid(column=1, row=2, columnspan=2)
email_e.insert(0, "jakub.banach@poczta.onet.pl")
pass_e = Entry(width=33)
pass_e.grid(column=1, row=3, sticky=E)

window.mainloop()
