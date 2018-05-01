import time

class StopWatch:
    def __init__(self):
        self.__startTime = time.time()
    def start(self):
        self.__startTime = time.time()
    def stop(self):
        self.__endTime = time.time()
    def getStartTime(self):
        return self.__startTime
    def getEndTime(self):
        return self.__endTime
    def getElapsedTime(self):
        print(self.getEndTime(), self.getStartTime())
        return ((self.getEndTime() - self.getStartTime()))

s = StopWatch()
sum = 0
for i in range(1, 1000001):
    sum += i
s.stop()
print("경과시간 : ", s.getElapsedTime())