temperatureAndHumidity.py
# to run this program press f5 on your keyboard
# If that does not work, go to the Run menu > Run module.

## add this line on top of file
# !/usr/bin/python

# imports from sensehat library
from sense_hat import SenseHat
# imports from time library
from time import sleep
import time

# defines 'sense' as referencing SenseHat from sense_hat library
sense = SenseHat()

r = (255, 0, 0) # red
o = (255, 127, 0) # orange
y = (255, 255, 0) # yellow
g = (0, 255, 0) # green
c = (0, 255, 255) # cyan
b = (0, 0, 255) # blue
i = (75, 0, 130) # indigo
v = (159, 0, 255) # violet
w = (255, 255, 255) # white
e = (0, 0, 0)  # e stands for empty/black

# --- defines 'temp' as current temprature
# temp = sense.temperature
# --- defines 'temp1' as temp to one decimal place
# temp1 = round(temp, 1)

# --- prints current temperature (temp) in python shell
# print (str(temp))
# --- prints current temperature to one decimal place (temp1) in python shell
# print (str(temp1))
# --- prints current temperature (temp) + units (˚C) in python shell
# print (str(temp) + "˚C")
# --- prints current temperature to one decimal place (temp1) + units (˚C) in python shell
# print (str(temp1) + "˚C")

# --- scrolls (on sense hat) current temperature to one decimal place (temp1) + units (˚C) in python shell
# sense.show_message (str(temp1) + "'C")

# To show a message in a specified colour...
# e.g. sense.show_message("hello", text_colour=(255, 255, 0)

oldTemp = 0.0
oldHumi = 0.0
st = 0.1 # defines sleep times st = short time, mt = medium time & bt = big time
mt = 1
bt = 100 # To achieve a 2 minute gap between readings, assuming that st=0.1 and mt=1, then bt must
         # be set to... 100

         # to update every x minutes, set bt to (x * 60) - 20

    
def tempTell():
    localtime = time.asctime( time.localtime(time.time()) )
    global oldTemp
    temp=sense.temperature
    temp1 = round(temp, 1)
    tempChange = temp1 - oldTemp
    tDiff = round(tempChange,1)
    if tDiff > 0:       
        print ("The temperature on", str(localtime), "is", str(temp1)+"˚C")
        print ("up by", float(tDiff),"˚C")
        sense.show_message (str(temp1) + "'C", text_colour=o)
        sleep(st)
        sense.show_message (str(temp1) + "'C", text_colour=o)
    elif tDiff < 0:
        tDiff = tDiff - (2*tDiff)
        print ("The temperature on", str(localtime), "is", str(temp1)+"˚C")
        print ("down by", float(tDiff),"˚C")
        sense.show_message (str(temp1) + "'C", text_colour=c)
        sleep(st)
        sense.show_message (str(temp1) + "'C", text_colour=c)
    else:
        print ("The temperature on", str(localtime), "is", str(temp1)+"˚C")
        print ("no change")
        sense.show_message (str(temp1) + "'C", text_colour=w)
        sleep(st)
        sense.show_message (str(temp1) + "'C", text_colour=w)
    print()
    oldTemp = temp1
    
def humidTell():
    localtime = time.asctime( time.localtime(time.time()) )
    global oldHumi
    humi = sense.humidity
    humi1 = round(humi, 1)
    humiChange = humi1 - oldHumi
    hDiff = round(humiChange, 1)
    if hDiff > 0:       
        print ("The humidity on", str(localtime), "is", str(humi1)+"%")
        print ("up by", float(hDiff),"%")
        sense.show_message (str(humi1) + "%", text_colour=o)
        sleep(st)
        sense.show_message (str(humi1) + "%", text_colour=o)
    elif hDiff < 0:
        hDiff = hDiff - (2*hDiff)
        print ("The humidity on", str(localtime), "is", str(humi1)+"%")
        print ("down by", float(hDiff),"%")
        sense.show_message (str(humi1) + "%", text_colour=c)
        sleep(st)
        sense.show_message (str(humi1) + "%", text_colour=c)
    else:
        print ("The humidity on", str(localtime), "is", str(humi1)+"%")
        print ("no change")
        sense.show_message (str(humi1) + "%", text_colour=w)
        sleep(st)
        sense.show_message (str(humi1) + "%", text_colour=w)
    print()
    oldHumi = humi1

tempHot  = [
    r,r,r,r,o,o,y,y,
    r,r,r,o,o,y,y,w,
    r,r,o,o,y,y,w,w,
    r,o,o,y,y,w,w,c,
    o,o,y,y,w,w,c,c,
    o,y,y,w,w,c,c,c,
    y,y,w,w,c,c,c,b,
    y,w,w,c,c,c,b,b,
    ]

tempMed  = [
    r,r,r,o,o,y,y,w,
    r,r,o,o,y,y,w,w,
    r,o,o,y,y,w,w,c,
    o,o,y,y,w,w,c,c,
    o,y,y,w,w,c,c,c,
    y,y,w,w,c,c,c,b,
    y,w,w,c,c,c,b,b,
    w,w,c,c,c,b,b,b,
    ]

tempCold  = [
    r,r,o,o,y,y,w,w,
    r,o,o,y,y,w,w,c,
    o,o,y,y,w,w,c,c,
    o,y,y,w,w,c,c,c,
    y,y,w,w,c,c,c,b,
    y,w,w,c,c,c,b,b,
    w,w,c,c,c,b,b,b,
    w,c,c,c,b,b,b,b,
    ]

humid1  = [
    b,b,b,b,b,c,c,c,
    b,b,b,b,c,c,c,c,
    b,b,b,b,c,c,c,c,
    b,b,b,c,c,c,c,w,
    b,c,c,c,c,w,w,w,
    c,c,c,c,w,w,w,w,
    c,c,c,c,w,w,w,w,
    c,c,c,w,w,w,w,w,
    ]

humid2  = [
    b,b,b,b,c,b,c,c,
    b,b,b,c,b,c,c,c,
    b,b,c,b,c,c,c,w,
    b,c,b,c,c,c,w,c,
    c,b,c,c,c,w,c,w,
    b,c,c,c,w,c,w,w,
    c,c,c,w,c,w,w,w,
    c,c,w,c,w,w,w,w,
    ]

clearScreen = [
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    ]

def humidCome():
    sense.set_pixels(humid1)
    sleep(0.3)
    sense.set_pixels(humid2)
    sleep(0.3)
    sense.set_pixels(humid1)
    sleep(0.3)
    sense.set_pixels(humid2)
    sleep(0.3)
    sense.set_pixels(humid1)
    sleep(0.3)
    sense.set_pixels(humid2)
    sleep(0.3)
    sense.set_pixels(clearScreen)

def tempCome():
    sense.set_pixels(tempHot)
    sleep(0.3)
    sense.set_pixels(tempMed)
    sleep(0.3)
    sense.set_pixels(tempCold)
    sleep(0.3)
    sense.set_pixels(tempMed)
    sleep(0.3)
    sense.set_pixels(clearScreen)



print ("Welcome to Pablo's temperature and humidity readout...")
print ()
sense.show_message ("Hello world!")
sleep(st)
tempCome()
localtime = time.asctime( time.localtime(time.time()) )
oldTemp
temp=sense.temperature
temp1 = round(temp, 1)
tempChange = temp1 - oldTemp
tDiff = round(tempChange,1)
print ("The temperature on", str(localtime), "is", str(temp1)+"˚C")
sense.show_message (str(temp1) + "'C")
sleep(st)
sense.show_message (str(temp1) + "'C")
oldTemp = temp1
print ()
sleep(mt)
humidCome()
localtime = time.asctime( time.localtime(time.time()) )
oldHumi
humi = sense.humidity
humi1 = round(humi, 1)
humiChange = humi1 - oldHumi
hDiff = round(humiChange, 1)
print ("The humidity on", str(localtime), "is", str(humi1)+"%")
sense.show_message (str(humi1) + "%")
sleep(st)
sense.show_message (str(humi1) + "%")
print ()
oldHumi = humi1
sleep(bt)
while True:
    tempCome()
    sleep(st)
    tempTell()
    sleep(mt)
    humidCome()
    humidTell()
    sleep(bt)
    
    

# forever loop
""" while True:
    # defines 'temp' as current temprature
    temp = sense.temperature
    # defines 'temp1' as temp to one decimal place
    temp1 = round(temp, 1)
    # prints current temperature to one decimal place (temp1) + units (˚C) in python shell
    print (str(temp1) + "˚C")
    # scrolls (on sense hat) current temperature to one decimal place (temp1) + units (˚C) in python shell
    sense.show_message (str(temp1) + "'C", text_colour=(255, 255, 0))
    # wait 5 seconds
    sleep(5) """




