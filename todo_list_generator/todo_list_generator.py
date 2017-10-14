import re
from pycolor import PyColor

class TodoListGenerator:
    def __init__(self):
        self.todo_list = []
        self.start_time = self.__get_start_time()

    def create_todo_list(self):
        while True:
            self.__add_todo()
            self.__return_todo_list()
            self.start_time = self.end_time

    def __add_todo(self):
        self.end_time = self.__get_end_time(self.__get_process_time())
        todo_name = self.__get_todo_name()
        if todo_name == "休憩":
            self.todo_list.append("\n{2} ({0} ~ {1})\n".format(self.__format_time(self.start_time), self.__format_time(self.end_time), todo_name))
        else:
            self.todo_list.append(" - [ ] {0} ~ {1} | {2}".format(self.__format_time(self.start_time), self.__format_time(self.end_time), todo_name))

    def __return_todo_list(self):
        print("-" * 100)
        for todo in self.todo_list:
            print(todo)
        print("-" * 100)

    def __get_todo_name(self):
        while True:
            todo_name = input(PyColor.CYAN + "TODO名 : " + PyColor.END)
            if todo_name: # 空文字でなければ
                return todo_name
            else:
                print(PyColor.RED + "TODO名を入力してください。" + PyColor.END)

    def __get_process_time(self):
        while True:
            process_time = input(PyColor.CYAN + "TODOにかかる時間(分) : " + PyColor.END)
            if re.match("^[0-9]{1,3}$", process_time):
                return int(process_time)
            else:
                print(PyColor.RED + "整数値3桁までで入力してください。" + PyColor.END)

    def __get_start_time(self):
        while True:
            start_time = input(PyColor.CYAN + "開始時間(HHMM) : " + PyColor.END)
            if re.match("^[0-9]{4}$", start_time):
                return start_time
            else:
                print(PyColor.RED + "整数値4桁で入力してください。" + PyColor.END)

    def __get_end_time(self, todo_process_minute):
        end_time = self.__calc_end_time(todo_process_minute)
        end_time_hour, end_time_minute = self.__convert_to_hour_and_minute(end_time)
        return "{0:02d}{1:02d}".format(end_time_hour, end_time_minute)

    def __format_time(self, time):
        return "{0:02d}:{1:02d}".format(int(time[:2]), int(time[2:]))

    def __calc_end_time(self, todo_process_minute):
        start_time_hour, start_time_minute = int(self.start_time[:2]) * 60, int(self.start_time[2:])
        end_time = start_time_hour + start_time_minute + todo_process_minute
        return end_time

    def __convert_to_hour_and_minute(self, time):
        return time // 60, time % 60

todo_list_generator = TodoListGenerator()
todo_list_generator.create_todo_list()
