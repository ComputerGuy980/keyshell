#!/usr/bin/env python3

import keysdec
import sys
import os
from time import sleep

NULL = chr(0)
hidbytes = NULL*8
buffer = []
lastKey = None
mode = 0

def unpress():
    hidbytes = NULL*8

def output(code,modifier=NULL):
    hidbytes = modifier + NULL*2 + code + NULL*4
    buffer.append(hidbytes)
    unpress()

def flush():

    global buffer
    buffer.append(NULL*8)
    
    with open('/dev/hidg0', 'rb+') as kb:
        for c in buffer:
            kb.write(c.encode())
            sleep(0.05)
        buffer = []

##    for c in buffer:
##        #os.system("echo -ne \"" + c + "\" > /dev/hidg0")
##        print(c.encode())
##        sleep(0.05)
##    buffer = []

print("Keyshell for Raspberry Pi Zero")
print("Press CTRL-C to quit")
print("Press enter on an empty line to switch between action and typing modes")
print("act codes: n - ENTER, e - ESC, b - DEL, t - TAB, s - secondary SPACE")

while True:
    try:
        if mode == 0:
            lastKey = None
            command = input("keyshell> ")

            if command == "":
                mode = 1
                continue
            
            for current in command:
                if current == lastKey:
                    output(chr(0)) #create gap between double letters
                if keysdec.getChr(current) != None:
                    output(keysdec.getChr(current))
                else:
                    if keysdec.getUpChr(current) != None:
                        output(keysdec.getUpChr(current),chr(32))
                    else:
                        print("unrecognized character: " + current)
                        break
                lastKey = current
            flush()
        else:
            lastKey = None
            command = input("keyshell act> ")

            if command == "":
                mode = 0
                continue
            
            for current in command:
                if current == lastKey:
                    output(chr(0)) #create gap between double presses
                if keysdec.getAct(current) != None:
                    output(keysdec.getAct(current))
                else:
                    print("unrecognized character: " + current)
                    break
                lastKey = current
            flush()
    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit()
