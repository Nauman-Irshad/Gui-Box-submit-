import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    gender = gender_var.get()
    country = country_var.get()
    

    messagebox.showinfo("Form Submitted", f"Name: {name}\nAge: {age}\nEmail: {email}\nGender: {gender}\nCountry: {country}")


root = tk.Tk()
root.title("User Registration Form")
root.geometry("300x350")  


tk.Label(root, text="_______________________Name_____________________").pack()
name_entry = tk.Entry(root)
name_entry.pack()


tk.Label(root, text="_______________________Age_______________________").pack()
age_entry = tk.Entry(root) 
age_entry.pack()


tk.Label(root, text="_______________________Email_______________________").pack()
email_entry = tk.Entry(root)
email_entry.pack()


tk.Label(root, text="Gender:").pack()
gender_var = tk.StringVar(value="None") 
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()


tk.Label(root, text="_______________________Country_______________________").pack()
country_var = tk.StringVar(value="Select Country")
country_menu = tk.OptionMenu(root, country_var, "USA", "UK", "Canada", "Australia")
country_menu.pack()

tk.Button(root, text="Submit", command=submit_form).pack(pady=10)

root.mainloop()
