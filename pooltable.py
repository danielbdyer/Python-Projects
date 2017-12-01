import json, sys, itertools, time, math
import datetime

dateOfRecord = datetime.datetime.strftime(datetime.datetime.now(),'%m-%d-%Y')
filename = (str(dateOfRecord) + '.json')

class PoolTable(object):
    num = itertools.count(1)

    def __init__(self):
        self.num = self.num.next()
        self.occupied = "NOT OCCUPIED"
        self.minutes = None
        self.start_time = None
        self.stop_time = None
        self.time_elapsed = None

        ####################

    def giveOut(self):
            self.checkOccupied()
            self.startTimer()
            return self.occupied

    def checkOccupied(self):
        if self.occupied == "OCCUPIED":
            print "Pooltable " + str(self.num) + " is currently occupied."
        else:
            self.occupied = "OCCUPIED"
            return self.occupied

    def startTimer(self):
        self.start_time = datetime.datetime.now()
        return self.start_time

        ####################

    #def checkTimer(self):
        #self.time_elapsed = datetime.datetime.now() - self.start_time
        #return self.time_elapsed

        ####################

    def closeOut(self):
        self.occupied = "NOT OCCUPIED"
        self.stopTimer()
        self.gatherTimeElapsed()
        self.readableTime()
        self.incurredCost()
        self.writeEntry()
        return self.occupied

    def stopTimer(self):
        self.stop_time = datetime.datetime.now()

    def gatherTimeElapsed(self):
        #if self.start_time != None:
        if self.stop_time != None:
            self.time_elapsed = self.stop_time - self.start_time
        else:
            #self.time_elapsed = checkTimer()
            self.time_elapsed = datetime.datetime.now() - self.start_time
        self.seconds = self.time_elapsed.total_seconds()
        self.minutes = self.seconds / 60
        print self.minutes
        #else:
            #self.stop_time = datetime.datetime.now()
            #self.start_time = self.stop_time - datetime.timedelta(minutes=self.minutes)
            #self.time_elapsed = self.stop_time - self.start_time
            #return self.minutes

    def viewVariables(self):
        try:
            print self.minutes
        except AttributeError:
            print "self.minutes does not exist"
        try:
            print self.start_time
        except AttributeError:
            print "self.start_time does not exist"
        try:
            print self.stop_time
        except AttributeError:
            print "self.stop_time does not exist"
        try:
            print self.time_elapsed
        except AttributeError:
            print "self.time_elapsed does not exist"
        try:
            print self.cost
        except AttributeError:
            print "self.cost does not exist"

    def readableTime(self):
        if self.minutes < 60:
            self.formatted_time_elapsed = "{0}min".format(int(self.minutes))
            return self.formatted_time_elapsed
        else:
            self.hours = math.floor(self.minutes / 60)
            self.plusminutes = self.minutes - (self.hours * 60)
            self.formatted_time_elapsed = "{0}hr{1}min".format(int(self.hours),int(self.plusminutes))
            return self.formatted_time_elapsed

    def incurredCost(self):
        self.cost = self.minutes * .5
        return "${:.2f}".format(self.cost)

    def writeEntry(self):
        with open(filename, 'w') as file_object:
            json.dump(self.toDictionary(), file_object, sort_keys=True, indent=4)

    def toDictionary(self):
        return {"Pool Table Number":self.num,"Start Date Time":str(self.start_time),"End Date Time":str(self.stop_time),"Total Time Played":self.gatherTimeElapsed()}

        ####################

    def getStatus(self):
        #if self.minutes is not None:
            #print "Pool Table {0}: {1} for {2}".format(str(self.num),str(self.occupied),str(self.readableTime()))
        #else:
        if self.occupied == "OCCUPIED":
            print "Pool Table {0}: {1} for {2}".format(str(self.num),str(self.occupied),str(self.gatherTimeElapsed()))
        else: # 'Not Occupied'
            print "Pool Table {0}: {1}".format(str(self.num),str(self.occupied))
        return

        ####################

    #def stageTable(self,minutes):
        #if self.occupied == "OCCUPIED":
            #print "Pooltable " + str(self.num) + " is currently occupied."
        #else:
            #self.occupied = "OCCUPIED"
            #self.minutes = minutes
            #self.start_time = None
            #self.stop_time = None
        #return self.occupied, self.minutes

        ####################

def viewAllTables():
    for tables in pooltable:
        tables.getStatus()

pooltable = [ PoolTable() for i in range(12)]

#pooltable[4].stageTable(85)
#pooltable[6].stageTable(20)
#pooltable[1].stageTable(55)

while True:
    choice = raw_input('Please input command: ')
    if choice == 'q':
        print "\n"
        break
    else:
        result = eval(str(choice))
