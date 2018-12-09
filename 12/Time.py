from datetime import datetime, date
import datetime, re
day_pattern = re.compile(r'^[A-Z]([a-z]){2}$')
relesson = re.compile(r'^(?P<time>\d{2}:\d{2}'
                           r'    (?P<subject>[a-zA-z]+)    '
                           r'(?P<teacher>[a-zA-z ]+)$')
lesson = re.compile(r'^(?P<time>\d{2}:\d{2}(\-\d{2}:\d{2}))'
                           r'    (?P<subject>[a-zA-z]+)    '
                           r'(?P<teacher>[a-zA-z ]+)$')
class Lesson:
    def __init__(self, time=None, subject=None, teacher=None):
        self.time = time
        self.teacher = teacher
        self.subject = subject
lessonList = list()
def timeOfLearning(file):
    b = False
    newL = Lesson()
    for i in file:
        if b:
            a = i.splite("    ")
            times = a[0].splite("-")
            t = datetime.datetime.strptime(times[0], "%H:%M")
            newL.time = newL.time - t
        if re.match(lesson, i):
            a = i.splite("    ")
            times = a[0].splite("-")
            t = datetime.datetime.strptime(times[0], "%H:%M") - datetime.datetime.strptime(times[1], "%H:%M")
            lessonList.append(Lesson(t, a[1], a[2]))
            b = False
        elif re.match(relesson, i):
            b = True
            a = i.splite("    ")
            times = a[0].splite("-")
            t = datetime.datetime.strptime(times[0], "%H:%M")
            newL = Lesson(t, a[1], a[2])
            lessonList.append(newL)
def analize(what):
    d = {}
    if what == "subject":
        for i in lessonList:
            if i.subject in d:
                d[i] = d[i] + i.time
            else:
                d[i] = i.time
        print(d)
    elif what == "teacher":
        for i in lessonList:
            if i.teacher in d:
                d[i] = d[i] + i.time
            else:
                d[i] = i.time
        print(d)
    else:
        total_time = 0
        for i in lessonList:
            total_time = total_time + i.time
        print (total_time)
"""
Здесь надо указать, что необходимо найти
"""
WHAT = ""
if __name__ == '__main__':
    with open("data.txt", "r") as file:
        timeOfLearning(file)
    analize(WHAT)