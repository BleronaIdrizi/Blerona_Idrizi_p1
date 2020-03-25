#https://stackoverflow.com/questions/57640792/how-to-call-a-method-using-the-users-input-in-python

#1 cm = (1/30.48) ft = 0.0328084 ft
#cmToFeet
#https://www.sanfoundry.com/python-program-read-height-centimeters-covert-height-feet-inches/
cm=int(input("Enter the height in centimeters:"))
feet=0.0328*cm
print("The length in feet",round(feet,2))


#1 ft = 30.48 cm
#FeetToCm
#https://www.w3resource.com/python-exercises/python-basic-exercise-59.php
feett=int(input("Enter the height in feet:"))
cmm=30.48*feett
print("The length in centimeter is:",round(cmm,2))

#1 km = (1/1.609344) mi = 0.62137119 mi
#kmToMiles
#https://www.rapidtables.com/convert/length/km-to-mile.html
km=int(input("Enter the km:"))
mile=0.62137119*km
print("Mile are:",round(mile,2))

#1 mi = 1.609344 km
#MileToKm
#https://www.rapidtables.com/convert/length/mile-to-km.html
milee=int(input("Enter the mile:"))
kmm=1.609344*milee
print("km are:",round(kmm,2))