import sys
class Record:
    def __init__(self, hour, minute, second, distance):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.distance = distance
while True:
    time_dis = input()
    if time_dis == 0:
        break
    # if エラーが発生:
    #     sys.exit()