# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 09:44:00 2017

@author: martinhab
"""

import car


# Audi
aurs04 = Car("Audi RS6 plus", 2004, 174, 4.4, 82, "4WD", "PER", 2)
aurs04u = Car("Audi RS6 plus", 2004, 177, 4.1, 85, "4WD", "PER", 2)
#audi = [aurs04]
audi = [aurs04u]

# BMW
bm5304 = Car("BMW 530d", 2004, 155, 6.4, 75, "RWD", "STD", 2)
bm5304u = Car("BMW 530d", 2004, 168, 5.2, 83, "RWD", "STD", 2)
bmm596 = Car("BMW M5", 1996, 155, 4.9, 79, "RWD", "PER", 2)
bmm596u = Car("BMW M5", 1996, 159, 4.6, 82, "RWD", "PER", 2)
bmx516 = Car("BMW X5 40e (PHEV)", 2016, 130, 6.8, 69, "4WD", "ALL", 3)
bmx516u = Car("BMW X5 40e (PHEV)", 2016, 138, 5.6, 74, "4WD", "ALL", 3)
bmz800 = Car("BMW Z8", 2000, 155, 4.5, 77, "RWD", "PER", 1)
bmz800u = Car("BMW Z8", 2000, 164, 3.8, 85, "RWD", "PER", 1)
#bmw = [bm5304, bmm596, bmx516, bmz800]
bmw = [bm5304u, bmm596u, bmx516u, bmz800u]

# Caterham
case15 = Car("Caterham Seven 270", 2015, 122, 5.0, 77, "RWD", "PER", 1)
case15u = Car("Caterham Seven 270", 2015, 129, 4.2, 85, "RWD", "PER", 1)
ca2195 = Car("Caterham 21", 1995, 127, 6.7, 75, "RWD", "PER", 1)
#caterham = [case15]
caterham = [case15u, ca2195]

# Chevrolet
chtr06 = Car("Chevrolet Trailblazer SS", 2006, 142, 5.6, 62, "4WD", "ALL", 3)
chtr06u = Car("Chevrolet Trailblazer SS", 2006, 154, 4.5, 67, "4WD", "ALL", 3)
chca16 = Car("Chevrolet Camaro Z/28", 2016, 187, 4.0, 87, "RWD", "PER", 2)
chca16u = Car("Chevrolet Camaro Z/28", 2016, 190, 3.6, 90, "RWD", "PER", 2)
chch70 = Car("Chevrolet Chevelle SS 454", 1970, 130, 6.3, 57, "RWD", "STD", 2)
#chevrolet = [chtr06, chca16]
chevrolet = [chtr06u, chca16u, chch70]

# Citroen
cicc07 = Car("Citroen C-Crosser 2.2 L HDi", 2007, 124, 9.6, 70, "4WD", "ALL", 3)
cicc07u = Car("Citroen C-Crosser 2.2 L HDi", 2007, 128, 8.8, 75, "4WD", "ALL", 3)
#citroen = [cicc07]
citroen = [cicc07u]

# Ford
fosi86 = Car("Ford Sierra RS Cosworth", 1986, 143, 6.2, 78, "RWD", "PER", 2)
fosi86u = Car("Ford Sierra RS Cosworth", 1986, 151, 5.1, 87, "RWD", "PER", 2)
fomo17 = Car("Ford Mondeo", 2017, 135, 8.3, 80, "FWD", "STD", 2)
#ford = [fosi86]
ford = [fosi86u, fomo17]


# Lotus
loel03 = Car("Lotus Elise Sport 135", 2003, 129, 5.1, 85, "RWD", "PER", 1)
loel03u = Car("Lotus Elise Sport 135", 2003, 137, 4.3, 94, "RWD", "PER", 1)
#lotus = [loel03]
lotus = [loel03u]

# McLaren
loel03 = Car("McLaren 12C", 2011, 207, 3.0, 89, "RWD", "PER", 1)
mclaren = [loel03]

# Mercedes-Benz
mee594 = Car("Mercedes E 500", 1994, 155, 5.8, 74, "RWD", "PER", 2)
mee594u = Car("Mercedes E 500", 1994, 167, 4.6, 80, "RWD", "PER", 2)
mecl15 = Car("Mercedes CLS 400", 2015, 155, 5.1, 78, "RWD", "STD", 2)
mecl15u = Car("Mercedes CLS 400", 2015, 159, 4.7, 81, "RWD", "STD", 2)
#mercedes = [mee594, mecl15]
mercedes = [mee594u, mecl15u]

# Nissan
da2469 = Car("Datsun 240Z Rally Car", 1969, 144, 6.3, 80, "RWD", "OFF", 1)
da2469u = Car("Datsun 240Z Rally Car", 1969, 152, 5.2, 89, "RWD", "OFF", 1)
nimu02 = Car("Nissan Murano GT-C", 2002, 140, 7.7, 77, "4WD", "ALL", 3)
nimu02u = Car("Nissan Murano GT-C", 2002, 148, 6.5, 80, "4WD", "ALL", 3)
niqa16 = Car("Nissan Qashqai", 2016, 113, 11.5, 77, "FWD", "ALL", 3)
#nissan = [da2469, nimu02]
nissan = [da2469u, nimu02u, niqa16]


# Renault
re5t80 = Car("Renault 5 Turbo", 1980, 130, 6.3, 76, "RWD", "PER", 1)
re5t80u = Car("Renault 5 Turbo", 1980, 137, 5.2, 84, "RWD", "PER", 1)
re2186 = Car("Renault 21 2.0l Turbo Quadra", 1986, 138, 7.8, 75, "4WD", "PER", 2)
re2583 = Car("Renault 25 V6 Turbo", 1983, 137, 7.3, 71, "FWD", "STD", 2)
#renault = [re5t80]
renault = [re5t80u, re2186, re2583]


# Subaru
sule16 = Car("Subaru Levorg", 2016, 130, 8.9, 78, "4WD", "ALL", 2)
sule16u = Car("Subaru Levorg", 2016, 137, 7.2, 87, "4WD", "ALL", 2)
suwr14 = Car("Subaru WRX STI", 2014, 159, 5.2, 85, "4WD", "PER", 2)
suwr14u = Car("Subaru WRX STI", 2014, 162, 4.8, 88, "4WD", "PER", 2)
#subaru = [sule16, suwr14]
subaru = [sule16u, suwr14u]

# Vauxhall
vamo16 = Car("Vauxhall Mokka 4x4", 2016, 111, 11.9, 68, "4WD", "STD", 3)
vauxhall = [vamo16]

# Build list of cars
cars = []



cars.extend(chevrolet)
cars.extend(caterham)

cars.extend(citroen)
cars.extend(ford)
cars.extend(lotus)
cars.extend(mclaren)
cars.extend(mercedes)

cars.extend(audi)
cars.extend(nissan)
cars.extend(renault)
cars.extend(subaru)

cars.extend(bmw)
cars.extend(vauxhall)





checkedCars = []
topOfTreeCars = []

print("Unchecked cars:")
for car in cars:
    print (car.name)

print("")    

for car in cars:
    print("Checking car " + car.name)
    dominated = False
    if len(checkedCars) > 0:
        for otherCar in topOfTreeCars:
            compare(car, otherCar)
        
    # if car has not been dominated
    if len(car.domb) == 0:
        topOfTreeCars.append(car)
        print("Not dominated. Added to top of tree.")
        
    checkedCars.append(car)
    print("\t" + car.name + " added to checked cars")

    # clean top-of-tree list
    
    removal = []
    for topCar in topOfTreeCars:
        if len(topCar.domb) > 0:
            print("Removing " + topCar.name)
            removal.append(topCar)
    for removeCar in removal:
        topOfTreeCars.remove(removeCar)
#    
    print("\nDominance hierarchy:")
    topCopy = topOfTreeCars
    for printCar in topCopy:
        print (printCar.name)
        for otherCar in printCar.doms:
            print("\t" +otherCar.name)
            if len(otherCar.doms) > 0:
                for subCar in otherCar.doms:
                    print("\t\t" + subCar.name)
                    if len(subCar.doms) > 0:
                        for subSubCar in subCar.doms:
                            print("\t\t\t" + subSubCar.name)
                            if len(subSubCar.doms) > 0:
                                for subSubSubCar in subSubCar.doms:
                                    print("\t\t\t\t" + subSubSubCar.name)
    
    print("")
    print("---------\n")

print("Finished adding cars")
print(len(checkedCars))
 
# To be changed:
# Implement database connection (SQL or MongoDB)
