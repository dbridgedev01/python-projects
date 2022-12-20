from tkinter import *
from tkinter import messagebox
from password_genrator import generate_password
import json
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_button_func():
    password = generate_password()
    pyperclip.copy(password)
    password_entry.delete(0, END)
    password_entry.insert(END, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_button_func():
    website = website_entry.get().title()
    email = username_entry.get()
    password = password_entry.get()

    new_data = {
        website:
            {
                "Email": email,
                "Password": password
            }
    }

    if not website or not email or not password:
        messagebox.showerror("Error", "Input Fields Are Empty!\n"
                                      "Please Check Your Inputs.")
    else:
        dialog = messagebox.askyesno("Save To File", message=f"Website: {website}\n\n"
                                                             f"Email/Username: {email}\n\n"
                                                             f"Password: {password}\n\n"
                                                             f"Do you want to save this "
                                                             f"information?")

        if dialog:
            try:
                with open(file="data.json", mode="r") as data_file:
                    # Load The Data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open(file="data.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Update The Data
                data.update(new_data)
                with open(file="data.json", mode="w") as data_file:
                    # Saving Data
                    json.dump(data, data_file, indent=4)
            finally:
                messagebox.showinfo("Success", "The Information Was Saved Successfully.")

                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()

# ---------------------------- SEARCH ------------------------------- #


def search_button_func():
    website = website_entry.get().title()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo("Error", message="Sorry, Data Not Found.")
    else:
        if website not in data:
            messagebox.showinfo("Error", message=f"No Data Found For '{website}'.")
        else:
            website_data = data[website]
            messagebox.showinfo("Saved Information", message=f"Website: {website}\n\n"
                                                             f"Email/Username: {website_data['Email']}\n\n"
                                                             f"Password: {website_data['Password']}")
            pyperclip.copy(website_data['Password'])


# ---------------------------- UI SETUP ------------------------------- #

def create_label(custom_text, row, column):
    label = Label(text=custom_text)
    label.grid(row=row, column=column)
    return label


def create_entry(row, column, width=35, columnspan=1):
    entry = Entry(width=width)
    entry.grid(row=row, column=column, columnspan=columnspan)
    return entry


window = Tk()
window.config(padx=20, pady=20)
window.title("Password Manager")

# ICON
canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

# Other Components

website_label = create_label("Website", 1, 0)
website_entry = create_entry(1, 1, width=21)
website_entry.focus()

search_button = Button(text="Search", command=search_button_func, width=13)
search_button.grid(row=1, column=2)

username_label = create_label("Email/Username", 2, 0)
username_entry = create_entry(2, 1, columnspan=2)
username_entry.insert(END, "testemail@gmail.com")

password_label = create_label("Password", 3, 0)
password_entry = create_entry(3, 1, width=21)

generate_button = Button(text="Generate Password", command=generate_button_func)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add To File", width=36, command=add_button_func)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
