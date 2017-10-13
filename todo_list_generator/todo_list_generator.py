import re

class TodoListGenerator:
    todo_list = []

    def __init__(self):
        self.todo_list = []
        self.start_time = self.__get_start_time()
        self.end_time = self.start_time

    def create_todo_list(self):
        while True:
            self.__add_todo()
            self.__return_todo_list()
            self.start_time = self.end_time

    def __add_todo(self):
        self.end_time = self.__get_end_time(int(input("TODOにかかる時間(分) : ")))
        todo_name = self.__get_todo_name()
        self.todo_list.append(" - [ ] {0} ~ {1} | {2}".format(self.__format_time(self.start_time), self.__format_time(self.end_time), todo_name))

    def __return_todo_list(self):
        for todo in self.todo_list:
            print(todo)

    def __get_todo_name(self):
        while True:
            todo_name = input("TODO名 : ")
            if todo_name: # 空文字でなければ
                return todo_name
            else:
                print("TODO名を入力してください。")

    def __get_start_time(self):
        while True:
            start_time = input("開始時間(HHMM) : ")
            if re.match("^[0-9]{4}$", start_time):
                return start_time
            else:
                print("整数値4桁で入力してください。")

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
