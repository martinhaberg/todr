# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 09:44:00 2017

@author: martinhab
"""

from car import Car, compare, compare_with_children


# Audi
auqu90 = Car("Audi quattro 20V", 1990, 143, 6.0, 77, "4WD", "PER", 2)
aurs04 = Car("Audi RS6 plus", 2004, 174, 4.4, 82, "4WD", "PER", 2)
aurs04u = Car("Audi RS6 plus", 2004, 177, 4.1, 85, "4WD", "PER", 2)

# BMW
bmm596 = Car("BMW M5", 1996, 155, 4.9, 79, "RWD", "PER", 2)
bmm596u = Car("BMW M5", 1996, 159, 4.6, 82, "RWD", "PER", 2)
bmx516 = Car("BMW X5 40e (PHEV)", 2016, 130, 6.8, 69, "4WD", "ALL", 3)
bmx516u = Car("BMW X5 40e (PHEV)", 2016, 138, 5.6, 74, "4WD", "ALL", 3)
bmz800 = Car("BMW Z8", 2000, 155, 4.5, 77, "RWD", "PER", 1)
bmz800u = Car("BMW Z8", 2000, 164, 3.8, 85, "RWD", "PER", 1)

# Chevrolet
chtr06 = Car("Chevrolet Trailblazer SS", 2006, 142, 5.6, 62, "4WD", "ALL", 3)
chtr06u = Car("Chevrolet Trailblazer SS", 2006, 154, 4.5, 67, "4WD", "ALL", 3)
chtr06a = Car("Chevrolet Trailblazer SS", 2006, 142, 5.6, 62, "4WD", "ALL", 3)
chca16 = Car("Chevrolet Camaro Z/28", 2016, 187, 4.0, 87, "RWD", "PER", 2)
chca16u = Car("Chevrolet Camaro Z/28", 2016, 190, 3.6, 90, "RWD", "PER", 2)

# Citroen

# Ford
fofo12 = Car("Ford Focus ST", 2017, 150, 6.5, 84, "FWD", "PER", 2)
fofo12u = Car("Ford Focus ST", 2017, 150, 6.5, 84, "FWD", "PER", 2)

# Honda
hons90 = Car("Honda NSX", 1990, 168, 5.7, 84, "RWD", "PER", 1)
hons90u = Car("Honda NSX", 1990, 171, 5.3, 87, "RWD", "PER", 1)

# Hummer
huh309 = Car("Hummer H3T", 2009, 97, 9.3, 65, "4WD", "OFF", 3)
huh309u = Car("Hummer H3T", 2009, 97, 9.3, 65, "4WD", "OFF", 3)

# Infiniti
inqx16 = Car("Infiniti QX50", 2016, 137, 6.4, 79, "RWD", "ALL", 3)
inqx16u = Car("Infiniti QX50", 2016, 137, 6.4, 79, "RWD", "ALL", 3)

# Lotus
loel03 = Car("Lotus Elise Sport 135", 2003, 129, 5.1, 85, "RWD", "PER", 1)
loel03u = Car("Lotus Elise Sport 135", 2003, 137, 4.3, 94, "RWD", "PER", 1)
loel02 = Car("Lotus Elise 111S", 2002, 132, 4.8, 80, "RWD", "PER", 1)
loel02u = Car("Lotus Elise 111S", 2002, 132, 4.8, 80, "RWD", "PER", 1)

# McLaren
mc1211 = Car("McLaren 12C", 2011, 207, 3.0, 89, "RWD", "PER", 1)
mc1211u = Car("McLaren 12C", 2011, 210, 2.8, 92, "RWD", "PER", 1)

# Mercedes-Benz
mecl15 = Car("Mercedes-Benz CLS 400", 2015, 155, 5.1, 78, "RWD", "STD", 2)
mecl15u = Car("Mercedes-Benz CLS 400", 2015, 159, 4.7, 81, "RWD", "STD", 2)
mec315 = Car("Mercedes-Benz C 350e", 2015, 155, 5.6, 75, "RWD", "STD", 2)
mec315u = Car("Mercedes-Benz C 350e", 2015, 155, 5.6, 75, "RWD", "STD", 2)
mes307 = Car("Mercedes-Benz S 350 4MATIC", 2007, 152, 7.5, 71, "4WD", "STD", 2)
mes307u = Car("Mercedes-Benz S 350 4MATIC", 2007, 152, 7.5, 71, "4WD", "STD", 2)

# Mini
mijo16 = Car("Mini John Cooper Works", 2016, 153, 6.0, 80, "FWD", "PER", 2)

# Nissan
nixt16 = Car("Nissan X-Trail", 2016, 116, 10.5, 78, "4WD", "ALL", 3)
da2469 = Car("Datsun 240Z Rally Car", 1969, 144, 6.3, 80, "RWD", "OFF", 1)
da2469u = Car("Datsun 240Z Rally Car", 1969, 152, 5.2, 89, "RWD", "OFF", 1)
nimu02 = Car("Nissan Murano GT-C", 2002, 140, 7.7, 77, "4WD", "ALL", 3)
nimu02u = Car("Nissan Murano GT-C", 2002, 148, 6.5, 80, "4WD", "ALL", 3)

# Subaru
sule16 = Car("Subaru Levorg", 2016, 130, 8.9, 78, "4WD", "ALL", 2)
sule16u = Car("Subaru Levorg", 2016, 137, 7.2, 87, "4WD", "ALL", 2)
suwr14 = Car("Subaru WRX STI", 2014, 159, 5.2, 85, "4WD", "PER", 2)
suwr14u = Car("Subaru WRX STI", 2014, 162, 4.8, 88, "4WD", "PER", 2)

# Renault
recl09 = Car("Renault Sport Clio 200", 2009, 134, 6.7, 85, "FWD", "PER", 2)

# Vauxhall
vavx00 = Car("Vauxhall VX220", 2000, 135, 5.6, 80, "RWD", "PER", 1)

# Volvo
vo8597 = Car("Volvo 850 AWD", 1997, 137, 7.2, 73, "4WD", "STD", 2)

# Populate RQ lists
# Original spec
rq13 = []
rq14 = [auqu90, recl09, vo8597]
rq15 = [nixt16, sule16]
rq16 = [chtr06, chtr06a, da2469, fofo12, inqx16, loel02, loel03, mes307, mijo16, vavx00]
rq18 = [bmm596, bmx516, hons90, huh309, mec315]; rq19 = [bmz800, nimu02]
rq21 = [mecl15, suwr14]; rq22 = [aurs04]; rq23 = [chca16]; rq25 = [mc1211]

# Upgraded spec
rq13u = []
rq14u = [auqu90, recl09, vo8597]
rq15u = [nixt16, sule16u]
rq16u = [chtr06u, chtr06a, da2469u, fofo12u, inqx16u, loel02u, loel03u, mes307u, mijo16, vavx00]
rq18u = [bmm596u, bmx516u, hons90u, huh309u, mec315u]; rq19u = [bmz800u, nimu02u]
rq21u = [mecl15u, suwr14u]; rq22u = [aurs04u]; rq23u = [chca16u]; rq25u = [mc1211u]

# Build list of cars
cars = []
# Original spec
# cars.extend(rq13); cars.extend(rq14); cars.extend(rq15); cars.extend(rq16)
# cars.extend(rq18); cars.extend(rq19)
# cars.extend(rq21); cars.extend(rq22); cars.extend(rq23);
# cars.extend(rq25)
# Upgraded spec
cars.extend(rq13u); cars.extend(rq14u); cars.extend(rq15u); cars.extend(rq16u)
cars.extend(rq18u); cars.extend(rq19u); cars.extend(rq21u); cars.extend(rq22u)
cars.extend(rq23u); cars.extend(rq25u)


checkedCars = []; topOfTreeCars = []

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
