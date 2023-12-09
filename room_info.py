import json
from tkinter import *
from color_palette import *
from tkinter import messagebox

class RoomInfo:

    def __init__(self):
        self.room_info_window = Toplevel()
        self.room_info_window.title("Room information")
        self.room_info_window.config(padx=20, pady=20, bg=ALMOND_FROST)

        # Canvas
        self.room_info_canvas = Canvas(self.room_info_window, width=800, height=400,
                                       bg=DONKEY_BROWN, highlightthickness=0)
        self.room_info_canvas.grid(column=0, row=0, padx=20, pady=20, columnspan=2)

        self.heading = self.room_info_canvas.create_text(200, 50, text="Room Info", font=FONT_TITLE,
                                                         width=300, fill="#fff")
        # Button inside Canvas

        get_btn_img = PhotoImage(file="img/get_btn_img.png")
        self.get_btn = Button(self.room_info_window, image=get_btn_img,
                              highlightthickness=0, borderwidth=0, activebackground=DONKEY_BROWN,
                              command=self.room_number_get)
        self.get_btn["bg"] = DONKEY_BROWN
        self.get_btn.place(x=100, y=200)

        # Button

        exit_btn_img = PhotoImage(file="img/exit_small_btn_img.png")

        self.exit_btn = Button(self.room_info_window, image=exit_btn_img, highlightthickness=0, borderwidth=0,
                               activebackground=ALMOND_FROST, command=self.room_info_window.destroy)
        self.exit_btn["bg"] = ALMOND_FROST
        self.exit_btn.grid(column=0, row=1, pady=10, padx=10)

        search_btn_img = PhotoImage(file="img/serach_btn_img.png")
        self.search_btn = Button(self.room_info_window, image=search_btn_img,
                                 highlightthickness=0, borderwidth=0,
                                 activebackground=ALMOND_FROST, command=self.show_data) ## in show_data, check date existence, if cannot find the date, need to throw warning box
        self.search_btn["bg"] = ALMOND_FROST
        self.search_btn.grid(column=1, row=1, pady=10, padx=10)

        # Entry, Label, Dropdown menu
        room_list = ["101", "102", "103", "104", "105","201","202","203","204","205","lab1", "lab2", "lab3", "Aud1","Aud2"]
        self.clicked = StringVar()
        self.clicked.set(room_list[0])
        self.room_number_label = Label(self.room_info_canvas, text="ROOM NUMBER:", font=FONT_TEXT,
                                       background=DONKEY_BROWN, foreground="#fff")
        self.room_number_label.place(x=75, y=100)

        self.room_number_dropdown = OptionMenu(self.room_info_window, self.clicked, *room_list)
        self.room_number_dropdown.place(x=280, y=125)
        # self.room_number_entry = Entry(self.room_info_canvas, width=40, highlightthickness=0, borderwidth=0)
        # self.room_number_entry.place(x=250, y=112)

        self.date_label = Label(self.room_info_canvas, text="DATE:", font=FONT_TEXT,
                                background=DONKEY_BROWN, foreground="#fff")
        self.date_label.place(x=75, y=135)

        self.date_entry = Entry(self.room_info_canvas, width=20, highlightthickness=0, borderwidth=0)
        self.date_entry.place(x=260, y=147)

        self.room_number_get_label = Label(self.room_info_canvas, text=room_list[0], font=FONT_TEXT,
                                           background=DONKEY_BROWN, foreground="#fff")
        self.room_number_get_label.place(x=255, y=172)

        self.data_label = Label(self.room_info_canvas, text="", font=FONT_TEXT,
                                background=DONKEY_BROWN, foreground="#fff")
        self.data_label.place(x=100, y=230)

        self.room_info_window.mainloop()

    def room_number_get(self):
        self.room_number_get_label.config(text=self.clicked.get())

    def show_data(self):
        room_list = self.search_mechanism()
        self.data_label.config(text=room_list)

    def search_mechanism(self):
        date = self.date_entry.get()  ## date input from user 
        room_number = self.room_number_get_label.cget("text")

        with open("room.json", "r") as datafile:
            data = json.load(datafile)
        ## check if the room has any event that day
        if not date in data[room_number]: 
            messagebox.showwarning(title="Oops", message="There is no event in that day.")
        else:
            time_data = data[room_number][date]
            room_list = [time for time in time_data]
            new_room_list = []
            for index in room_list:
                class_name = time_data[index]["class_name"]
                index = index + ": " + class_name
                new_room_list.append(index)

            new_room_list ='\n'.join(new_room_list)

            return new_room_list


