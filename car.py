# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 09:44:00 2017

@author: martinhab
"""

class Car:
    def __init__(self, name, rq, year, topspeed, acc, grip, drive, tyres, ride=None, tractrl=None, abs=None):
        self.name = name
        self.rq = int(rq)
        self.year = int(year)
        self.topspeed = int(topspeed)
        self.acc = float(acc)
        self.grip = int(grip)
        self.drive = drive.split()[0]
        self.tyres = tyres.split()[0]
        if ride == None:
            self.ride = 1
        else:
            self.ride = int(ride)

        if tractrl == None:
            self.tractrl = False
        elif tractrl.split()[0] == "yes":
            self.tractrl = True
        else:
            self.tractrl = False
        if abs == None:
            self.abs = False
        elif abs.split()[0] == "yes":
            self.abs = True
        else:
            self.abs = False

        self.doms = []
        self.domb = []

    def add_dominated_car(self, dominated_car):
        self.doms.append(dominated_car)

    def add_dominating_car(self, dominating_car):
        self.domb = [dominating_car]

    def rem_dominating_car(self):
        self.domb = []

def dominates(car1, car2):
    if car1.topspeed >= car2.topspeed:
        #print("Dominates TS")
        if car1.acc <= car2.acc:
            #print("Dominates acc")
            if car1.grip >= car2.grip:
                #print("Dominates grip")
                if car1.drive == "4WD" or car2.drive == "FWD" or (car2.drive == "RWD" and car1.drive != "FWD"):
                    #print("Dominates drive")
                    if car1.tyres == "OFF" or car2.tyres == "PER" or car2.tyres == "SLI" or car1.tyres == car2.tyres or (car1.tyres == "ALL" and car2.tyres == "STD"):
                        #print("Dominates tyres")
                        if car1.ride >= car2.ride:
                            #print("Dominates ride")
                            if car1.tractrl == True or car2.tractrl == False:
                                #print("Dominates traction control")
                                if car1.abs == True or car2.abs == False:
                                    #print("Dominates brakes")
                                    return True
    else:
        return False

def compare(newCar, otherCar):
    # first check if car is already placed
    if len(newCar.domb) > 0:
        return None

    # if newCar is dominated
    print("\tComparing " + newCar.name + " with " + otherCar.name)
    if dominates(otherCar, newCar):
        print("\t\t" + otherCar.name + " dominates " + newCar.name)
        # three possible cases:
        # 1) no children,
        if len(otherCar.doms) == 0:
            print("\t\t" + otherCar.name + " has no children")
            otherCar.add_dominated_car(newCar)
            newCar.add_dominating_car(otherCar)
            #print("\t\t\tComparison returns True")
            return True
        else:
            print("\t" + otherCar.name + " has children. Starts comparison:")
            # 2) no dominating children
            if compare_with_children(newCar, otherCar) == None:
                print("\t\tNo dominating children exist")
                otherCar.add_dominated_car(newCar)
                newCar.add_dominating_car(otherCar)
                #print("\t\t\tComparison returns True")
                return True
            #else:
                # 3) at least one dominating child
                #print("\t\tAt least one dominating child exists")




            # add new car as child if no other children present

    elif dominates(newCar, otherCar):
        print("\t\t" + newCar.name + " dominates " + otherCar.name)

        # remove link from any earlier dominating car
        if len(otherCar.domb) > 0:
            otherCar.domb[0].doms.remove(otherCar)

        # add new link
        otherCar.add_dominating_car(newCar)
        #print("Now dominated by " + otherCar.domb[0].name)
        newCar.add_dominated_car(otherCar)



        #print("\t\t\tComparison returns true")
        return True

    else:
        print("\t\tNo car dominates")
        #print("\t\t\tComparison returns None")
        return None

def compare_with_children(newCar, otherCar):
    checkList = []
    for addCar in otherCar.doms:
        checkList.append(addCar)

    for childCar in checkList:
        # check if newCar is dominated
        compare(newCar, childCar)
        #if result == False:
        #    return_value = None
        #elif result == True:
        #    return_value =  childCar
        if len(newCar.domb) > 0:
            return newCar.domb[0]

    else:
        return None
