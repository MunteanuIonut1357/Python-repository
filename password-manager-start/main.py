from tkinter import *
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    text_box3.delete(0,END)
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    text_box3.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def search_password():
    site=text_box1.get()
    try:
        with open("data.json","r") as data_file:
            dict=json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="File not found!")
    else:
        found=False
        for key,value in dict.items():
            if key==site:
                messagebox.showinfo(title=site,message=f"Email: {dict[key]['mail']} | password: {dict[key]['password']}")
                pyperclip.copy(dict[key]['password'])
                found=True
        if found==False:
            messagebox.showinfo(title="Faied",message="Site does not exist!")

def save_password():
    site = text_box1.get()
    mail = text_box2.get()
    password = text_box3.get()
    new_data={site:{"mail":mail,
                    "password":password
                    }
              }
    text=site+" | "+mail +" | "+password
    if len(site) > 0 and len(mail) > 0 and len(password) > 0:
        is_ok = messagebox.askokcancel(title="Are you sure about changes?", message=text)
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data=json.load(file)

            except FileNotFoundError:
                with open("data.json","w") as file:
                    json.dump(new_data,file,indent=4)
            except ValueError:
                with open("data.json","w") as file:
                    json.dump(new_data,file,indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data,file,indent=4)
            finally:
                text_box1.delete(0, END)
                text_box2.delete(0, END)
                text_box3.delete(0, END)
                messagebox.showinfo(message="Data successfully added!")
        else:
            messagebox.showinfo(message="Data was not added!")
    else:
        messagebox.showinfo(message="Error empty boxes!")


# ---------------------------- UI SETUP ------------------------------- #

screen = Tk()

screen.title("Password Manager")

screen.config(padx=30, pady=30, bg="gray")

canvas = Canvas(width=500, height=169, bg="gray", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(300, 92, image=lock_img)
canvas.grid(row=0, column=0, columnspan=3)

Website_label = Label(text="Website:", bg="gray", fg="white", width=20, height=3)
Website_label.grid(row=1, column=0, sticky="w")

text_box1 = Entry(width=40)
text_box1.grid(row=1, column=1)
text_box1.focus()

Website_label = Label(text="Email/Username:", bg="gray", fg="white", width=20, height=3)
Website_label.grid(row=2, column=0, sticky="w")

text_box2 = Entry(width=40)
text_box2.grid(row=2, column=1)

Website_label = Label(text="Password:", bg="gray", fg="white", width=20, height=3)
Website_label.grid(row=3, column=0, sticky="w")

text_box3 = Entry(width=40)
text_box3.grid(row=3, column=1)

generate_buttons = Button(text="Generate password", width=25, command=generate_password)
generate_buttons.grid(row=2, column=3)
add_button = Button(text="Add password", width=34, command=save_password)
add_button.grid(row=4, column=1)
search_button = Button(text="Search password", width=25, command=search_password)
search_button.grid(row=1, column=3)

screen.mainloop()
