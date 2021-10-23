import time


class Timer:
    def get_week(self):
        now_time = time.localtime()
        now_week = now_time.tm_wday
        return now_week

    def get_now_hour(self):
        now_time = time.localtime()
        now_hour = now_time.tm_hour
        return now_hour

    def get_next_hour(self):
        now_time = time.localtime()
        last_hour = now_time.tm_hour
        if last_hour == 23:
            last_hour = 0
        else:
            last_hour = last_hour + 1
        return last_hour

    def get_now_min(self):
        now_time = time.localtime()
        now_min = now_time.tm_min
        return now_min

    def get_now_second(self):
        now_time = time.localtime()
        now_second = now_time.tm_sec
        return now_second

    def get_now_time(self):
        now_time = time.strftime("%H:%M")
        print(now_time)

    def get_next_time(self):
        now_time = time.localtime()
        hour = self.get_next_hour()
        min = time.strftime(":%M")
        if hour >= 0 and hour <= 9:
            hour = '0' + str(hour)
        now_time = str(hour) + min
        print(now_time)
        return now_time


timer = Timer()
timer.get_next_time()

