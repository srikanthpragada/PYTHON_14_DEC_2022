import json


class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s


t = Time(10, 20, 30)
s = json.dumps(t.__dict__)  # Convert dict to json
print(s)

times = [Time(1, 2, 3), Time(10, 10, 10)]
times_dict = [t.__dict__ for t in times]
print(json.dumps(times_dict))

