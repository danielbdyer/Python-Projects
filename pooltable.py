import json, sys, itertools, time, math, io, os, datetime, smtplib

dateOfRecord = datetime.datetime.strftime(datetime.datetime.now(),'%m-%d-%Y')
filename = (str(dateOfRecord) + '.json')

if not os.path.isfile(filename) and not os.access(filename, os.R_OK):
    with io.open(filename, 'w', encoding='utf-8') as file_object:
        file_object.write(unicode([]))

pooltable = []

class PoolTable(object):
    num = itertools.count(1)

    def __init__(self):
        self.num = self.num.next()
        self.occupied = "NOT OCCUPIED"
        self.minutes = None
        self.seconds = None
        self.start_time = None
        self.stop_time = None
        self.time_elapsed = None

        ####################

    def giveOut(self):
        if self.occupied == "NOT OCCUPIED":
            self.occupied = "OCCUPIED"
            self.startTimer()
            return self.occupied
        else:
            print "Pooltable " + str(self.num) + " is currently occupied."
            return "Pooltable " + str(self.num) + " is currently occupied."

    def startTimer(self):
        self.start_time = datetime.datetime.now()
        return self.start_time

        ####################

    def closeOut(self):
        if self.occupied == "OCCUPIED":
            self.occupied = "NOT OCCUPIED"
            self.stopTimer()
            self.gatherTimeElapsed()
            self.incurredCost()
            self.writeEntry()
            return self.occupied
        else:
            print "Pooltable " + str(self.num) + " has already been closed out."
            return "Pooltable " + str(self.num) + " has already been closed out."

    def stopTimer(self):
        self.stop_time = datetime.datetime.now()
        return self.stop_time

        ####################

    def gatherTimeElapsed(self):
        if self.stop_time != None:
            self.time_elapsed = self.stop_time - self.start_time
        else:
            self.time_elapsed = datetime.datetime.now() - self.start_time
        self.seconds = self.time_elapsed.total_seconds()
        self.minutes = self.seconds / 60
        timestr = self.readableTime()
        return timestr

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

        ####################

    def writeEntry(self):
        with open(filename, 'r') as file_object:
            arrayOfDictionaries = json.load(file_object)
        with open(filename, 'w') as file_object:
            arrayOfDictionaries.append(self.toDictionary())
            json.dump(arrayOfDictionaries, file_object, sort_keys=True, indent=4)

    def toDictionary(self):
        return {"Pool Table Number":self.num,"Start Date Time":str(self.start_time),"End Date Time":str(self.stop_time),"Total Time Played":self.gatherTimeElapsed()}

        ####################

    def getStatus(self):
        if self.occupied == "OCCUPIED":
            print "Pool Table {0}: {1} for {2}".format(str(self.num),str(self.occupied),str(self.gatherTimeElapsed()))
        else: # 'Not Occupied'
            print "Pool Table {0}: {1}".format(str(self.num),str(self.occupied))
        return

        ####################

pooltable = [ PoolTable() for i in range(12)]

def viewAllTables():
    for tables in pooltable:
        tables.getStatus()
