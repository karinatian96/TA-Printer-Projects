import random

from pythonds.basic import Queue #need to download the pythonds first, or write another def Queue function

class Printer: #reference to the basic structure on the textbook
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getProcessingTime() * 60/self.pagerate

class Task: #reference to the basic structure on the textbook
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,30)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp

class OfficeHourRequest: #reference to the basic structure on the textbook
    def __init__(self, time):
        self.timestamp = time
        self.processingTime = random.randrange(1,30)

    def getStamp(self):
        return self.timestamp

    def getProcessingTime(self):
        return self.processingTime

    def waitTime(self, currenttime):
        return currenttime - self.timestamp

def officeHourSimulation(numSeconds, requestPerMinute): #reference to the basic structure on the textbook

    TA = Printer(requestPerMinute)
    requestQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):

      if newRequest():
         request = OfficeHourRequest(currentSecond)
         requestQueue.enqueue(request)

      if (not TA.busy()) and (not requestQueue.isEmpty()):
        nextrequest = requestQueue.dequeue()
        waitingtimes.append(nextrequest.waitTime(currentSecond))
        TA.startNext(nextrequest)

      TA.tick()

    averageWait=sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,requestQueue.size()))
    
def newRequest(): #reference to the basic structure from textbook
    num = random.randrange(1,150)
    if num == 149:
        return True
    else:
        return False

for i in range(20):
    officeHourSimulation(3600,5)
