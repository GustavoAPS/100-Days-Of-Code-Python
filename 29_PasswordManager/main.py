from tkinter import *


# ----------------------- PASSWORD GENERATOR --------------------- #

# ----------------------- SAVE PASSWORD -------------------------- #

# ----------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
lock_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

web_site_label = Label(text="Website:")
web_site_label.grid(row=1, column=0)
web_site_entry = Entry()
web_site_entry.grid(row=1, column=1, columnspan=2)

email_label = Label(text="Email/UserName:")
email_label.grid(row=2, column=0)
email_entry = Entry()
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry()
password_entry.grid(row=3, column=1, columnspan=1)
password_button = Button(text="Generate Password")
password_button.grid(row=3, column=2, columnspan=1)

add_button = Button(text="Add")
add_button.grid(row=4, column=1, columnspan=3)


window.mainloop()
