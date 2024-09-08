# Data entry (Version 0.0.0)
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# window 
window = tk.Tk()
window.title('Data entry Menu')
window.geometry('700x450')
window.config(bg = '#CDC9C9')
window.iconbitmap("Data entry enterface\logo.ico")


# Confirm data function
def confirm_data():
  accept_cond = accept_cond_var.get()
  if accept_cond == 'accepted' :
      # User info :
      First_name = First_name_entry.get()
      Last_name = Last_name_entry.get()
      if First_name and Last_name : # just by like that we can check if the string is empty or not
        Title = Title_combobox.get()
        Age = Age_spinbox.get()
        Nationality = Nationality_combobox.get()

        # Course info
        Registration = Registration_var.get()
        Completed_courses = Completed_courses_spinbox.get()
        Semesters = Semesters_spinbox.get()

        # acceptance 
        # accept_cond = accept_cond_checkbutton.get()
        print('-----------------------------------------------------------------------')
        print(f'First name = {First_name} | Last name = {Last_name}')
        print(f'Title = {Title} | Age = {Age} | Nationality : {Nationality}')
        print(f'# Completed courses : {Completed_courses} | # Semesters : {Semesters}')
        print(f'Registration status : {Registration}')
        print('-----------------------------------------------------------------------')
      else :
         tk.messagebox.showwarning(title = 'Error', message = 'First name and Last name are required !')
  else : 
     tk.messagebox.showwarning(title = 'Error', message = 'You should accept the terms and conditions !')


# User Interface (first Labelframe)
User_Interface = tk.LabelFrame(window, text = 'User Interface', relief = 'groove', font = "Calibri 20 bold")

# Define the widgets
First_name_label = ttk.Label(User_Interface, text = 'First Name *', font = 'Arial 12 bold')
First_name_entry = ttk.Entry(User_Interface)

Last_name_label = ttk.Label(User_Interface, text = 'Last name *', font = 'Arial 12 bold')
Last_name_entry = ttk.Entry(User_Interface)

Title_label = ttk.Label(User_Interface, text = 'Title', font = 'Arial 12 bold')
Title_combobox = ttk.Combobox(User_Interface, values = ('Noob','Pro','Haker'))

Age_label = ttk.Label(User_Interface, text = 'Age', font = 'Arial 12 bold')
Age_var = tk.IntVar(value = 18)
Age_spinbox = ttk.Spinbox(User_Interface, from_ = 18, to = 110, textvariable = Age_var)

Nationality_label = ttk.Label(User_Interface, text = 'Nationality', font = 'Arial 12 bold')
Nationality_combobox = ttk.Combobox(User_Interface, values = ('Amarican','French','Tunisian'))

# grid division (4 rows x 3 columns)
User_Interface.rowconfigure((0,1,2), weight = 1)
User_Interface.columnconfigure((0,1,2,3), weight = 1)

First_name_label.grid(row = 0, column = 0) 
First_name_entry.grid(row = 1, column = 0, pady = 5) 

Last_name_label.grid(row = 0, column = 1)
Last_name_entry.grid(row = 1, column = 1, pady = 5)

Title_label.grid(row = 0, column = 2)
Title_combobox.grid(row = 1, column = 2, pady = 5)

Age_label.grid(row = 2, column = 0)
Age_spinbox.grid(row = 3, column = 0, pady = 5)

Nationality_label.grid(row = 2, column = 1)
Nationality_combobox.grid(row = 3, column = 1, pady = 5)

User_Interface.pack(expand = True, fill = 'both', padx = 10, pady = 10)

# Status Interface (Second Labelframe)
Status_Interface = tk.LabelFrame(window, text = 'Status Interface', relief = 'groove', font = "Calibri 20 bold")

# Define the widgets
Registration_label = ttk.Label(Status_Interface, text='Registration', font = 'Arial 12 bold')

Registration_var = tk.StringVar(value = 'Not registred')
Registration_checkbutton = tk.Checkbutton(Status_Interface, 
                                          variable = Registration_var, 
                                          onvalue = 'Registred', 
                                          offvalue = 'Not Registred', 
                                          text='Currently Registered', 
                                          font = 'Arial 12 bold')

Completed_courses_label = ttk.Label(Status_Interface, text='# Completed courses', font = 'Arial 12 bold')
Completed_courses_var = tk.IntVar(value = 0)
Completed_courses_spinbox = ttk.Spinbox(Status_Interface,textvariable = Completed_courses_var,  from_=0, to=100)  # You can set appropriate range

Semesters_label = ttk.Label(Status_Interface, text='# Semesters', font = 'Arial 12 bold')
semester_var = tk.IntVar(value = 0)
Semesters_spinbox = ttk.Spinbox(Status_Interface, textvariable = semester_var, from_=0, to=20)  # You can set appropriate range

# Grid division (2 rows x 3 columns)
Status_Interface.rowconfigure((0, 1), weight=1)
Status_Interface.columnconfigure((0, 1, 2), weight=1)

# Place the widgets in the grid
Registration_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
Registration_checkbutton.grid(row=1, column=0, padx=5, pady=5, sticky='w')

Completed_courses_label.grid(row=0, column=1, padx=5, pady=5, sticky='ew')
Completed_courses_spinbox.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

Semesters_label.grid(row=0, column=2, padx=5, pady=5, sticky='ew')
Semesters_spinbox.grid(row=1, column=2)

Status_Interface.pack(expand = True, fill = 'both', padx = 10)

# Terms and Conditions (Third Labelframe)
Terms_and_conditions = tk.LabelFrame(window, text = 'Terms and Conditions', 
                                     relief = 'groove', 
                                     font = "Calibri 20 bold")

# Define the widgets
accept_cond_var = tk.StringVar(value = 'Not accepted')
accept_cond_checkbutton = tk.Checkbutton(Terms_and_conditions, 
                                         variable = accept_cond_var,
                                         onvalue = 'accepted',
                                         offvalue = 'Not accepted',
                                         text = 'I accept the terms and conditions . *', 
                                         font = 'Arial 12')
accept_cond_checkbutton.pack(side = 'left')

Terms_and_conditions.pack(expand = True, fill = 'both', padx = 10, pady = 10)

# Button of confirmation 
confirmation_button = tk.Button(window, text = 'Confirm', 
                                font = 'Arial 12 bold', 
                                bg = '#838B8B', 
                                fg = '#F0F8FF',
                                command = confirm_data)
confirmation_button.pack(fill = 'x', padx = 10, pady = 10)


# run
window.mainloop()