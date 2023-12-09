import json
import pandas as pd
from tkinter import *
from color_palette import *


class TimeTable:
    def __init__(self):
        self.time_table_window = Toplevel()
        self.time_table_window.title("Time Table")
        self.time_table_window.config(padx=20, pady=20, bg=ALMOND_FROST)

        get_btn_img = PhotoImage(file="img/get_btn_img.png")

        class_list = self.get_class_id()
        self.clicked_class = StringVar()
        self.clicked_class.set(class_list[0])
        self.class_id_label = Label(self.time_table_window, text="CLASS ID:", font=FONT_TEXT,
                                    background=ALMOND_FROST, foreground="#fff")
        self.class_id_label.grid(column=0, row=0, padx=10, pady=10)
        self.class_id_dropdown = OptionMenu(self.time_table_window, self.clicked_class, *class_list)
        self.class_id_dropdown.grid(column=1, row=0, padx=10, pady=10)
        self.get_class_btn = Button(self.time_table_window, image=get_btn_img,
                                    highlightthickness=0, borderwidth=0, activebackground=ALMOND_FROST,
                                    command=self.class_id_label_get)
        self.get_class_btn["bg"] = ALMOND_FROST
        self.get_class_btn.grid(column=2, row=0, padx=10, pady=10)

        self.get_class_label = Label(self.time_table_window, text="", font=FONT_TEXT,
                                     background=ALMOND_FROST, foreground="#fff")
        self.get_class_label.grid(column=3, row=0, padx=10, pady=10)

        self.clicked_date = StringVar()
        self.date_label = Label(self.time_table_window, text="DATE:", font=FONT_TEXT,
                                background=ALMOND_FROST, foreground="#fff")
        self.date_dropdown = ""
        self.get_date_btn = Button(self.time_table_window, image=get_btn_img,
                                   highlightthickness=0, borderwidth=0,
                                   activebackground=ALMOND_FROST, command=self.date_label_get)
        self.get_date_label = Label(self.time_table_window, text="", font=FONT_TEXT,
                                    background=ALMOND_FROST, foreground="#fff")
        self.get_date_btn["bg"] = ALMOND_FROST

        search_btn_img = PhotoImage(file="img/serach_btn_img.png")
        self.search_btn = Button(self.time_table_window, image=search_btn_img, highlightthickness=0, borderwidth=0,
                                 activebackground=ALMOND_FROST, command=self.print_timetable)
        self.search_btn["bg"] = ALMOND_FROST
        self.search_btn.grid(column=0, row=2, padx=10, pady=10, columnspan=4)
        self.timetable = Label(self.time_table_window, text="", font=FONT_TEXT,
                               background=ALMOND_FROST, foreground="#fff", justify=RIGHT)
        self.timetable.grid(column=0, row=3, padx=10, pady=10, columnspan=4)
        self.time_table_window.mainloop()
# choose 
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

    def class_id_label_get(self):
        self.get_class_label.config(text=self.clicked_class.get())
        date_list = self.get_date(self.get_class_label.cget("text"))
        self.date_dropdown = OptionMenu(self.time_table_window, self.clicked_date, *date_list)
        self.date_label.grid(column=0, row=1, padx=10, pady=10)
        self.date_dropdown.grid(column=1, row=1, padx=10, pady=10)
        self.get_date_btn.grid(column=2, row=1, padx=10, pady=10)
        self.get_date_label.grid(column=3, row=1, padx=10, pady=10)

    def date_label_get(self):
        self.get_date_label.config(text=self.clicked_date.get())

    def gen_time_table(self, class_id, date):

        with open("data.json", "r") as file:
            data = json.load(file)

        data_list_parent = []
        tuple_list = []
        for time in data[class_id][date]:
            data_list = [data[class_id][date][time]["class name"],
                         data[class_id][date][time]["instructor"],
                         data[class_id][date][time]["total time"],
                         data[class_id][date][time]["room number"]]
            tuple_child = [(time, "Event"), (time, "Instructor"),
                           (time, "Total Time"), (time, "Room Number")]
            tuple_list += tuple_child
            data_list_parent += data_list
        data_list_parent = [data_list_parent]
        cols = pd.MultiIndex.from_tuples(tuple_list)
        df = pd.DataFrame(data_list_parent, columns=cols)
        df = df.T
        df = str(df)
        df = df.split('\n')
        df.pop(0)
        df = '\n'.join(df)
        return df

    def print_timetable(self):
        df = self.gen_time_table(self.get_class_label.cget("text"), self.get_date_label.cget("text"))
        self.timetable.config(text=df)
