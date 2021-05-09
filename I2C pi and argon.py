import smbus
import time
from random import randint

#variables
channel = 1
address = 0x10 #listen on adress 0x10

#bus
bus = smbus.SMBus(channel)

#Read byte data
def ReadByte():
    reading = bus.read_byte_data(address, 1)
    return reading
    
#loop until key interupt
while True:   
    data = ReadByte()
    if(data <= 10):
        print("Too Dark, " + "Light Level: " +  str(data))
    elif(data > 10) and (data <= 25):
        print("Dark, " + "Light Level: " +  str(data))
    elif(data > 25) and (data <= 50):
        print("Medium, " + "Light Level: " +  str(data))
    elif(data > 50) and (data <= 75):
        print("Bright, " + "Light Level: " +  str(data))
    else:
        print("Too Bright, " + "Light Level: " + str(data))        
    time.sleep(10) # wait for 10 seconds