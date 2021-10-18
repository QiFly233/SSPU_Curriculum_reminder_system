import time


class Timer:
    def __init__(self):
        now_time = time.localtime()
        self.now_week = now_time.tm_wday
        self.now_hour = now_time.tm_hour
        self.now_min = now_time.tm_min
        self.now_second = now_time.tm_sec

    def get_week(self):
        return self.now_week

    def get_now_hour(self):
        return self.now_hour

    def get_last_hour(self):
        last_hour = self.now_hour
        if last_hour == 0:
            last_hour = 23
        else:
            last_hour = last_hour - 1
        return last_hour

    def get_now_second(self):
        print(self.now_second)

