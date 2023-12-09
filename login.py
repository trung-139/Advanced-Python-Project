import tkinter as tk
import json
from homepage import HomePageUI
from student import StudentUI
from color_palette import *
class Login:
    def __init__(self, root):
        
        self.window = root
        self.window.title("Login")
        self.window.geometry("800x500+0+0")
        self.window.config(padx=20, pady=20, bg=ALMOND_FROST)

        self.login_frame = tk.Frame(
            self.window,  
            bg=ALMOND_FROST, 
            relief=tk.GROOVE
        )        
        self.login_frame.place(x=0, width=1540, height=700)

        self.login_text = tk.Label(
            self.login_frame, 
            text="Login", 
            font=FONT_TEXT, 
            background=ALMOND_FROST, 
            foreground="#fff")
        self.login_text.place(x=120, y=100)

        self.login_username_lab = tk.Label(
            self.login_frame, 
            text="Username: ",
            font=FONT_TEXT, 
            background=ALMOND_FROST, 
            foreground="#fff")
        self.login_username_lab.place(x=120, y=135)

        self.login_username_entry = tk.Entry(
            self.login_frame, 
            font=("Times New Roman", 13),
            )
        self.login_username_entry.place(x=300, y=135, width=250, height=30)

        self.login_password_lab = tk.Label(
            self.login_frame,
            text="Password: ",
            font=FONT_TEXT, 
            background=ALMOND_FROST, 
            foreground="#fff")
        self.login_password_lab.place(x=120, y=170)

        self.login_password_entry = tk.Entry(
            self.login_frame,
            font=("Times New Roman", 13),
            show="*", 
            )
        self.login_password_entry.place(x=300, y=170, width=250, height=30)
        
        self.submit_button = tk.Button(
            self.login_frame,
            text="Submit",
            font=FONT_TEXT, 
            background=ALMOND_FROST, 
            foreground="#fff",
            width=20,
            relief=tk.FLAT,
            command=self.login_submit
        )
        self.submit_button.place(x=300, y=300)

    def login_submit(self):
        # read the username and password data from user_data.txt
        with open("user_data.txt", "r") as f:
            user_data = f.read().splitlines()

        # loop through each line in the file and check if login credentials are valid
        valid_credentials = False 
        self.student_major = None  # set default value for student_major
        for line in user_data:  # check if user exists in user list
            if line.count(':') == 2:
                username, password, role_with_id = line.strip().split(":")
                role_parts = role_with_id.split("-")
                role_type = role_parts[0]
                if len(role_parts) > 1:
                    # If there is an ID, extract it
                    role_id = role_parts[1]
                if role_type == "a":
                    # This is an admin user
                    if self.login_username_entry.get() == username and self.login_password_entry.get() == password:
                        valid_credentials = True
                        self.role = "admin"
                        self.role_id = role_id  
                        self.username = username
                        break
                elif role_type == "s":
                    # This is a student user
                    if self.login_username_entry.get() == username and self.login_password_entry.get() == password:
                        valid_credentials = True
                        self.role = "student"
                        self.student_major = role_parts[1]  # extract the student role
                        self.username = username
                        break

        # show error message if login credentials are invalid
        if not valid_credentials:
            error_label = tk.Label(self.login_frame, text="Invalid username or password", font=("Times New Roman", 13), fg="red")
            error_label.place(x=350, y=240)
        else:
            # create and show the appropriate window based on the user's role
            if self.role == "admin":
                self.window.destroy()  # destroy the login window
                obj = HomePageUI()  # create a new instance of Teacher class to show the teacher window
            elif self.role == "student":
                self.window.destroy()  # destroy the login window
                obj = StudentUI(self.student_major)  # create a new instance of Student class to show the student window
