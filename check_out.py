import json
from tkinter import *
from color_palette import *
from tkinter import messagebox

class CheckOut:

    def __init__(self):
        self.check_out_window = Toplevel()
        self.check_out_window.title("Remove")
        self.check_out_window.config(padx=20, pady=20, bg=ALMOND_FROST)

        get_btn_img = PhotoImage(file="img/get_btn_img.png")

        # Class ID
        class_list = self.get_class_id()
        self.clicked_class = StringVar()
        self.clicked_class.set(class_list[0])
        self.class_id_label = Label(self.check_out_window, text="CLASS ID:", font=FONT_TEXT,
                                    background=ALMOND_FROST, foreground="#fff")
        self.class_id_label.grid(column=0, row=0, padx=10, pady=10)
        self.class_id_dropdown = OptionMenu(self.check_out_window, self.clicked_class, *class_list)
        self.class_id_dropdown.grid(column=1, row=0, padx=10, pady=10)
        self.get_class_btn = Button(self.check_out_window, image=get_btn_img,
                                    highlightthickness=0, borderwidth=0, activebackground=ALMOND_FROST,
                                    command=self.class_id_label_get)
        self.get_class_btn["bg"] = ALMOND_FROST
        self.get_class_btn.grid(column=2, row=0, padx=10, pady=10)

        self.get_class_label = Label(self.check_out_window, text="", font=FONT_TEXT,
                                     background=ALMOND_FROST, foreground="#fff")
        self.get_class_label.grid(column=3, row=0, padx=10, pady=10)
        # Date
        self.clicked_date = StringVar()
        self.date_label = Label(self.check_out_window, text="DATE:", font=FONT_TEXT,
                                background=ALMOND_FROST, foreground="#fff")
        self.date_dropdown = ""
        self.get_date_btn = Button(self.check_out_window, image=get_btn_img,
                                   highlightthickness=0, borderwidth=0,
                                   activebackground=ALMOND_FROST, command=self.date_label_get)
        self.get_date_label = Label(self.check_out_window, text="", font=FONT_TEXT,
                                    background=ALMOND_FROST, foreground="#fff")
        self.get_date_btn["bg"] = ALMOND_FROST
        # Time

        self.clicked_time = StringVar()
        self.time_list = []
        self.time_label = Label(self.check_out_window, text="TIME:", font=FONT_TEXT,
                                background=ALMOND_FROST, foreground="#fff")
        self.time_dropdown = ""
        self.get_time_btn = Button(self.check_out_window, image=get_btn_img,
                                   highlightthickness=0, borderwidth=0,
                                   activebackground=ALMOND_FROST, command=self.time_label_get)
        self.get_time_label = Label(self.check_out_window, text="", font=FONT_TEXT,
                                    background=ALMOND_FROST, foreground="#fff")
        # Button
        exit_btn_img = PhotoImage(file="img/exit_btn_img.png")
        self.exit_btn = Button(self.check_out_window, image=exit_btn_img, highlightthickness=0, borderwidth=0,
                               activebackground=ALMOND_FROST, command=self.check_out_window.destroy)
        self.exit_btn["bg"] = ALMOND_FROST
        self.exit_btn.grid(column=0, row=3, columnspan=2, pady=10, padx=10)
        del_btn_img = PhotoImage(file="img/del_btn_img.png")
        self.del_btn = Button(self.check_out_window, image=del_btn_img, highlightthickness=0, borderwidth=0,
                              activebackground=ALMOND_FROST, command=self.del_class)
        self.del_btn["bg"] = ALMOND_FROST
        self.del_btn.grid(column=2, row=3, columnspan=2, pady=10, padx=10)
        self.check_out_window.mainloop()


    def get_class_id(self):
        with open("data.json", "r") as datafile:
            data = json.load(datafile)

        class_id_list = [class_id for class_id in data]
        return class_id_list

    def get_date(self, class_id):
        with open("data.json", "r") as datafile:
            data = json.load(datafile)

        date_list = [date for date in data[class_id]]
        return date_list

    def get_time(self, class_id, date):
        with open("data.json", "r") as datafile:
            data = json.load(datafile)
        time_list = [date for date in data[class_id][date]]
        return time_list

    def class_id_label_get(self):
        self.get_class_label.config(text=self.clicked_class.get())
        date_list = self.get_date(self.get_class_label.cget("text"))
        self.date_dropdown = OptionMenu(self.check_out_window, self.clicked_date, *date_list)
        self.date_label.grid(column=0, row=1, padx=10, pady=10)
        self.date_dropdown.grid(column=1, row=1, padx=10, pady=10)

        self.get_date_btn.grid(column=2, row=1, padx=10, pady=10)

        self.get_date_label.grid(column=3, row=1, padx=10, pady=10)

    def date_label_get(self):
        self.get_date_label.config(text=self.clicked_date.get())
        time_list = self.get_time(self.get_class_label.cget("text"), self.get_date_label.cget("text"))
        self.time_dropdown = OptionMenu(self.check_out_window, self.clicked_time, *time_list)
        self.time_label.grid(column=0, row=2, padx=10, pady=10)
        self.time_dropdown.grid(column=1, row=2, padx=10, pady=10)
        self.get_time_btn["bg"] = ALMOND_FROST
        self.get_time_btn.grid(column=2, row=2, padx=10, pady=10)
        self.get_time_label.grid(column=3, row=2, padx=10, pady=10)

    def time_label_get(self):
        self.get_time_label.config(text=self.clicked_time.get())

    def del_class(self):
        class_id = self.get_class_label.cget("text")
        date = self.get_date_label.cget("text")
        time = self.get_time_label.cget("text")

        with open("data.json", "r") as data_file_class:
            data = json.load(data_file_class)

        room_number = data[class_id][date][time]["room number"]
        class_name = data[class_id][date][time]["class name"]
        instructor = data[class_id][date][time]["instructor"]

        message = f"Do you want to delete the following reservation?\nClass ID: {class_id}\nDate: {date}\nTime: {time}\nClass Name: {class_name}\nInstructor: {instructor}\nRoom Number: {room_number}"
        response = messagebox.askyesno("Confirmation", message)
        if response == 1:
            del data[class_id][date][time]
            empty_data = {}
            if data[class_id][date] == empty_data:
                del data[class_id][date]
                if data[class_id] == empty_data:
                    del data[class_id]
            self.json_dump_data(data, "data.json")

            with open("room.json", "r") as data_file_room:
                data_room = json.load(data_file_room)

            del data_room[room_number][date][time]
            if data_room[room_number][date] == empty_data:
                del data_room[room_number][date]
            self.json_dump_data(data_room, "room.json")

            self.check_out_window.destroy()

    def json_dump_data(self, data, file_name):
        with open(file_name, "w") as data_file_class:
            json.dump(data, data_file_class, indent=4)
