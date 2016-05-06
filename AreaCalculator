"""This program will enable users to caculate circles and triangles areas"""
from math import pi
from time import sleep
from datetime import datetime
now = datetime.now()
print ("Hello! Lets have fun and calculate some areas!")
print ('Current time: %s/%s/%s %s:%s' % ((now.month), now.day, now.year, now.hour, now.minute))
sleep(1)
hint = raw_input("Don't forget to include the correct units!:")
option = raw_input ("Chose a shape: Type C for Circle and T for Triangle: ")
option = option.upper()
if option == "C":
  radius = float(raw_input("Enter radius:"))
  area = pi*(radius**2)
  print ("The pie is baking...")
  sleep(1)
  print ('The area of your circle is: %.2f %s' % (area, hint))
elif option == "T":
  base = float(raw_input("Enter base"))
  height = float(raw_input("Enter height"))
  area = base*height/2
  print ("Un Bi Tri...")
  sleep(1)
  print ('The area of your Triangle is: %.2f %s' % (area, hint))
else:
  print ("Wrong input, the program will now exit")
