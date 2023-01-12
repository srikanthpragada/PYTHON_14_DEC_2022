class Course:
    def __init__(self, title, duration, fee):
        self.title = title
        self.duration = duration
        self.fee = fee

    def show(self):
        print('Title : ', self.title)
        print('Duration : ', self.duration)
        print('Fee : ', self.fee)

    def getfee(self):
        return self.fee


class OnlineCourse(Course):
    def __init__(self, title, duration, fee, url):
        super().__init__(title, duration, fee)
        self.url = url

    # Overriding
    def show(self):
        super().show()
        print("URL : ", self.url)


class OfflineCourse(Course):
    def __init__(self, title, duration, fee, place):
        super().__init__(title, duration, fee)
        self.place = place

    # Overriding
    def show(self):
        super().show()
        print("Place : ", self.place)
        print("Old Student  : ", self.oldstudent)

    # Overriding
    def getfee(self, oldstudent=False):
        if oldstudent:
            return self.fee * 90 / 100
        else:
            return self.fee


online_c = OnlineCourse("Python", 30, 6000, "http://wyx")
offline_c = OfflineCourse("React", 20, 4000, "ST")

print(online_c.getfee())
print(offline_c.getfee())
print(offline_c.getfee(True))
