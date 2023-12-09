import json
from time_function import TimeFunction


class FileFunction(TimeFunction):

    def __init__(self):
        super().__init__()

    def class_data_input(self, data_pattern, file_name, date, class_id):

        try:
            with open(file_name, "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open(file_name, "w") as data_file:
                json.dump(data_pattern, data_file, indent=4)
        else:

            if class_id in data:
                if date in data[class_id]:
                    data_pattern = data_pattern[class_id][date]
                    data[class_id][date].update(data_pattern)
                else:
                    data_pattern = data_pattern[class_id]
                    data[class_id].update(data_pattern)
            else:
                data.update(data_pattern)
            with open(file_name, "w") as data_file:
                json.dump(data, data_file, indent=4)

    def compare_class_data(self, date, class_id, time_from, time_to):
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
        if class_id in data:
            if date in data[class_id]:
                for time_from_to in data[class_id][date]:
                    if not self.compare_room_time(time_from, time_to, time_from_to):
                        return False
        return True


    def room_data_update(self, room_number, data_pattern, date):

        with open("room.json", "r") as data_file:
            data = json.load(data_file)

        if self.room_number_exist(room_number):
            if date in data[room_number]:
                data_pattern = data_pattern[date]
                data[room_number][date].update(data_pattern)
            else:
                data[room_number].update(data_pattern)

        with open("room.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

    def compare_room_data(self, time_from, time_to, date, room_number):

        with open("room.json", "r") as data_file:
            data = json.load(data_file)

        if self.room_number_exist(room_number):
            if date in data[room_number]:
                for time_from_to in data[room_number][date]:
                    if not self.compare_room_time(time_from, time_to, time_from_to):
                        return False

        return True

    def compare_room_time (self, time_from, time_to, time_from_to):

        time_from_to = time_from_to.split("-")
        time_from_room = time_from_to[0]
        time_to_room = time_from_to[1]

        time_from = self.str_to_datetime(time_from)
        time_to = self.str_to_datetime(time_to)
        time_from_room = self.str_to_datetime(time_from_room)
        time_to_room = self.str_to_datetime(time_to_room)

        if time_to == time_to_room or time_from == time_from_room:
            return False
        elif time_to < time_to_room:
            if time_to > time_from_room:
                return False
        elif time_to > time_to_room:
            if time_from < time_to_room:
                return False

        return True

    def room_number_exist(self, room_number):

        with open("room.json", "r") as data_file:
            data = json.load(data_file)

        if room_number in data:
            return True

        return False
   