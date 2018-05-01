def compareTime(a,b):   #"08:59"이 "09:00보다 작다 = True
    hourA = int(a[0]) * 10 + int(a[1])
    minuteA = int(a[3])*10+int(a[4])
    hourB = int(b[0])*10+int(b[1])
    minuteB= int(b[3])*10+int(b[4])
    if hourA > hourB:
        return True
    elif hourA == hourB and minuteA > minuteB:
        return True
    else:
        return False
class Bus:
    def __init__(self,time):
        self.leavingTime = time
        self.customerLists = []

def shuttle(n, t, m, timetable):
    #step1 timetable을 버블정렬 : 비교 함수 필요
    for j in range(len(timetable)-1, 0, -1)
        for i in range(j):
            if compareTime((timetable[i],timetable[i+1])):
                temp = timetable[i+1]
                timetable[i+1] = timetable[i]
                timetable[i] = temp

    #step2 n개의 버스 객체 ( 출발시간, 승객명단) 생성
    busList = []
    hour = 9
    minute = 0
    time = "09:00"
    for i in range(n):
        busList.append(Bus(time))
        minute += t
        if minute > 59:
            hour += 1
            minute -= 60
        if hour < 10:
            time = "0" + str(hour)
        else:
            time = str(hour)
        if minute < 10:
            time =
    #step3 가장 마지막 배차된 버스의 승객이 꽉찼으면
    #       제일 마지막 승객 도착시간 -1 시간에 간다.
    #       꽉차지않았으면 마지막 배차버스 시간에 간다.