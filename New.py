from tkinter import *
from color_palette import *
from tkinter import messagebox
from time_function import TimeFunction
from file_function import FileFunction


class RoomNew(FileFunction, TimeFunction):

    def __init__(self):
        super().__init__()
        self.New_window = Toplevel()
        self.New_window.title("New")
        self.New_window.config(padx=20, pady=20, bg=ALMOND_FROST)

        # Canvas
        self.New_canvas = Canvas(self.New_window, width=800, height=400,
                                      bg=DONKEY_BROWN, highlightthickness=0)
        self.New_canvas.grid(column=0, row=0, padx=20, pady=20, columnspan=2)

        self.heading = self.New_canvas.create_text(400, 50, text="Create event", font=FONT_TITLE,
                                                        width=300, fill="#fff")

        # Canvas Entry and Label
        self.class_name_label = Label(self.New_canvas, text="EVENT (lesson):", font=FONT_TEXT,
                                      background=DONKEY_BROWN, foreground="#fff")
        self.class_name_label.place(x=75, y=100)

        self.class_name_entry = Entry(self.New_canvas, width=40, highlightthickness=0, borderwidth=0)
        self.class_name_entry.place(x=250, y=112)

        self.class_id_label = Label(self.New_canvas, text="CLASS ID:", font=FONT_TEXT,
                                    background=DONKEY_BROWN, foreground="#fff")
        self.class_id_label.place(x=75, y=135)

        self.class_id_entry = Entry(self.New_canvas, width=20, highlightthickness=0, borderwidth=0)
        self.class_id_entry.place(x=250, y=147)

        self.instructor_label = Label(self.New_canvas, text="INSTRUCTOR:", font=FONT_TEXT,
                                      background=DONKEY_BROWN, foreground="#fff")
        self.instructor_label.place(x=75, y=170)

        self.instructor_entry = Entry(self.New_canvas, width=40, highlightthickness=0, borderwidth=0)
        self.instructor_entry.place(x=250, y=182)

        self.date_label = Label(self.New_canvas, text="DATE:", font=FONT_TEXT,
                                background=DONKEY_BROWN, foreground="#fff")
        self.date_label.place(x=75, y=205)

        self.date_entry = Entry(self.New_canvas, width=20, highlightthickness=0, borderwidth=0)
        self.date_entry.place(x=250, y=217)
        self.date_entry.insert(0, "DD/MM/2023")

        self.time_from_label = Label(self.New_canvas, text="FROM:", font=FONT_TEXT,
                                     background=DONKEY_BROWN, foreground="#fff")
        self.time_from_label.place(x=75, y=240)

        self.time_from_entry = Entry(self.New_canvas, width=20, highlightthickness=0, borderwidth=0)
        self.time_from_entry.place(x=250, y=252)
        self.time_from_entry.insert(0, "06:00")

        self.time_to_label = Label(self.New_canvas, text="TO:", font=FONT_TEXT,
                                   background=DONKEY_BROWN, foreground="#fff")
        self.time_to_label.place(x=75, y=275)

        self.time_to_entry = Entry(self.New_canvas, width=20, highlightthickness=0, borderwidth=0)
        self.time_to_entry.place(x=250, y=287)
        self.time_to_entry.insert(0, "21:30")

        self.room_number_label = Label(self.New_canvas, text="ROOM NUMBER:", font=FONT_TEXT,
                                       background=DONKEY_BROWN, foreground="#fff")
        self.room_number_label.place(x=75, y=310)
        #replace entry by dropdown menu
        room_list = ["101", "102", "103", "104", "105","201","202","203","204","205","lab1", "lab2", "lab3", "Aud1","Aud2"]
        self.clicked = StringVar()
        self.clicked.set(room_list[0])

        self.room_number_dropdown = OptionMenu(self.New_window, self.clicked, *room_list)
        self.room_number_dropdown.place(x=280, y=335)

        # self.room_number_entry = Entry(self.New_canvas, width=20, highlightthickness=0, borderwidth=0)
        # self.room_number_entry.place(x=250, y=322)

        # Button inside canvas

        # room_list_small_btn_img = PhotoImage(file="img/room_list_small_btn.png")
        # self.room_list_small_btn = Button(self.New_window, image=room_list_small_btn_img,
        #                                   highlightthickness=0, borderwidth=0,
        #                                   activebackground=DONKEY_BROWN)
        # self.room_list_small_btn["bg"] = DONKEY_BROWN
        # self.room_list_small_btn.place(x=405, y=333)

        # Button outside

        exit_btn_img = PhotoImage(file="img/exit_btn_img.png")
        confirm_btn_img = PhotoImage(file="img/confirm_btn_img.png")

        self.exit_btn = Button(self.New_window, image=exit_btn_img, highlightthickness=0, borderwidth=0,
                               activebackground=ALMOND_FROST, command=self.New_window.destroy)
        self.exit_btn["bg"] = ALMOND_FROST
        self.exit_btn.grid(column=0, row=1, pady=20, padx=20)

        self.confirm_btn = Button(self.New_window, image=confirm_btn_img, highlightthickness=0, borderwidth=0,
                                  activebackground=ALMOND_FROST, command=self.save_data)
        self.confirm_btn["bg"] = ALMOND_FROST
        self.confirm_btn.grid(column=1, row=1, pady=20, padx=20)

        # Mainloop

        self.New_window.mainloop()

    def save_data(self):

        class_name = self.class_name_entry.get()
        class_id = self.class_id_entry.get()
        instructor = self.instructor_entry.get()
        date = self.date_entry.get()
        time_from = self.time_from_entry.get()
        time_to = self.time_to_entry.get()
        room_number = self.clicked.get()
        # room_number= self.room_number_entry.get()
        total_time = self.time_calculation(time_from, time_to)

        if len(class_id) == 0 or len(class_name) == 0 or len(instructor) == 0 or len(date) == 0 or len(time_from) == 0 or len(time_to) == 0 or len(room_number) == 0:
            messagebox.showwarning(title="Oops", message="Pls don't leave any fields empty")

        elif not self.date_validation(date) or not self.date_range_validation(date):
            messagebox.showwarning(title="Oops", message="Invalid date format!!")

        elif not self.time_format_validation(time_from) or not self.time_format_validation(time_to):
            messagebox.showwarning(title="Oops", message="Invalid time format!!")

        elif not self.time_input_validation(time_from, time_to):
            messagebox.showwarning(title="Oops", message="Invalid time input!!")

        elif not self.time_range_validation(time_from, time_to):
            messagebox.showwarning(title="Oops", message="Invalid time range!!"
                                                         " You can only register between 06:00 to 21:30")

        elif total_time > 4: ## limit duration of the event
            messagebox.showwarning(title="Oops", message="You can only "
                                                         "register a class with the total of 4 hour or less")

        elif not self.room_number_exist(room_number):
            messagebox.showwarning(title="Oops", message="This Room number does not exist")

        elif not self.compare_room_data(time_from, time_to, date, room_number) \
                or not self.compare_class_data(date, class_id, time_from, time_to):
            messagebox.showwarning(title="Oops", message="This time period for this room is already occupied")

        else:
            message = messagebox.askyesno(title="Are you sure?", message=f"Class Name: {class_name} \n"
                                                                         f"Class ID: {class_id} \n"
                                                                         f"Instructor: {instructor} \n"
                                                                         f"Date: {date} \n"
                                                                         f"From: {time_from} \n"
                                                                         f"To: {time_to} \n"
                                                                         f"Total Time: {total_time}hr \n"
                                                                         f"Room Number: {room_number} \n"
                                                                         f"Do you want to save?")
            if message:
                time_from_to = time_from + "-" + time_to
                class_data_pattern = {class_id: {date: {time_from_to: {"class name": class_name,
                                                                       "instructor": instructor, "date": date,
                                                                       "time from": time_from, "time to": time_to,
                                                                       "total time": total_time,
                                                                       "room number": room_number}}}}
                self.class_data_input(class_data_pattern, "data.json", date, class_id)
                room_data_pattern = {date: {time_from_to: {"class_id": class_id, "class_name": class_name}}}
                self.room_data_update(room_number, room_data_pattern, date)
                self.New_window.destroy()

