
from tkinter import *
from color_palette import *
from New import RoomNew
from room_info import RoomInfo
from check_out import CheckOut
from timetable import TimeTable

class HomePageUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Room Management System")
        self.window.config(padx=20, pady=20, bg=ALMOND_FROST)

        New_btn_img = PhotoImage(file="img/Add_schedule_but.png")
        check_out_btn_img = PhotoImage(file="img/Delete_schedule_but.png") 
        room_info_btn_img = PhotoImage(file="img/room_information_but.png")
        timetable_btn_img = PhotoImage(file="img/Timetable_but.png")
        #class_info_btn_img = PhotoImage(file="img/class_info_img.png")
        exit_btn_img = PhotoImage(file="img/exit_button.png")

        # Label
        self.welcome_label = Label(text="Welcome", font=("Arial", 24, "bold"), bg=ALMOND_FROST, fg="#fff")
        self.welcome_label.grid(columnspan=2, column=0, row=0, pady=(20, 0))

        # Button
        self.New_btn = Button(self.window, image=New_btn_img, highlightthickness=0, borderwidth=0,
                                   activebackground=ALMOND_FROST, command=self.New_window)
        self.New_btn["bg"] = ALMOND_FROST
        self.New_btn.grid(column=0, row=1, padx=20, pady=20)

        self.room_info_btn = Button(self.window, image=room_info_btn_img, highlightthickness=0, borderwidth=0,
                                    activebackground=ALMOND_FROST, command=self.room_info_window)
        self.room_info_btn["bg"] = ALMOND_FROST
        self.room_info_btn.grid(column=0, row=2, padx=20, pady=20)

        self.check_out_btn = Button(self.window, image=check_out_btn_img, highlightthickness=0, borderwidth=0,
                                    activebackground=ALMOND_FROST, command=self.check_out_window)
        self.check_out_btn["bg"] = ALMOND_FROST
        self.check_out_btn.grid(column=1, row=1, padx=20, pady=20)

        self.timetable_btn = Button(self.window, image=timetable_btn_img, highlightthickness=0, borderwidth=0,
                                    activebackground=ALMOND_FROST, command=self.time_table_window)
        self.timetable_btn["bg"] = ALMOND_FROST
        self.timetable_btn.grid(column=1, row=2, padx=20, pady=20)

        self.exit_btn = Button(self.window, image=exit_btn_img, highlightthickness=0, borderwidth=0,
                               activebackground=ALMOND_FROST, command=self.window.destroy)
        self.exit_btn["bg"] = ALMOND_FROST
        self.exit_btn.grid(columnspan=2, column=0, row=3, padx=20, pady=(20, 0), sticky="we")

        # Add extra columns and rows around the buttons
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_rowconfigure(2, weight=1)
        self.window.mainloop()

    def New_window(self):
        New = RoomNew() 

    def room_info_window(self):
        room_info = RoomInfo()

    def check_out_window(self):
        check_out = CheckOut()

    def time_table_window(self):
        timetable = TimeTable()






