from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v','w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R','S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]  # generate a list of random letters

    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]  # generate a list of random symbols

    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]  # generate a list of random numbers

    password_list = password_letters + password_symbols + password_numbers  # concatenate all three lists into one list

    shuffle(password_list)  # shuffles the list

    password = "".join(password_list)  # joins all the elements in the list with "" as separator

    password_entry.insert(0, password)

    pyperclip.copy(password)  # copies the generated password onto the clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered : \nEmail: {email} "
                                                              f"\nPassword: {password} \nis it ok to save?")

        if is_ok:
            with open("data.txt", 'a') as file:
                file.write(f"{website} | {email} | {password}" + "\n")  # use data entries
                website_entry.delete(0, 'end')  # clears the website entry field
                password_entry.delete(0, 'end')  # clears the password entry field


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()  # create window
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)  # create Canvas
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)  # loads canvas on the screen

# Labels
website_label = Label(text="Website: ", bg="white")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username: ", bg="white")
email_label.grid(column=0, row=2)
password_label = Label(text="Password: ", bg="white")
password_label.grid(column=0, row=3)

# Entries

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")  # sticky="EW" makes so that widget fill entire column
website_entry.focus()  # focus the cursor on that entry
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(0, "abc@gmail.com")  # insert the string passed as second argument at the index 0 of the entry
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")

# Button
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="EW")
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
