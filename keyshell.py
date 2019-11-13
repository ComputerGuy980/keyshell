#!/usr/bin/env python3

print("starting keyshell...")

import keysdec
import sys
#from time import sleep

NULL = chr(0)

device = "/dev/hidg0"

hidbytes = NULL*8
buffer = []

lastKey = None

mode = 0
speed = False

lastFlag = None

for arg in sys.argv[1:]: # discards name of program, sys.argv[0]
    if arg[0] == "-": # flag
        if lastFlag != "d":
            if arg[1] == "f": # fast mode - less accurate...
                speed = True
                print("speed mode on with -f flag")
            elif arg[1] == "d": # select different
                lastFlag = "d"
                continue
            else:
                print("error: unrecognized flag: " + str(arg))
                sys.exit(1)
        else:
            print("error: no value given after -d flag")
            sys.exit(1)
    else:
        if lastFlag == "d":
            device = arg
        else:
            print("error: unrecognized argument: " + str(arg))
            sys.exit(1)

if lastFlag == "d":
    print("error: no value given after -d flag")
    sys.exit(1)  

if speed:
    def output(code,modifier=NULL):
        with open(device, 'rb+') as kb:
            hidbytes = modifier + NULL*2 + code + NULL*4
            kb.write(hidbytes.encode())
        #print(hidbytes.encode())
else:
    def output(code,modifier=NULL):
        hidbytes = modifier + NULL*2 + code + NULL*4
        buffer.append(hidbytes)
        unpress()

def unpress():
    hidbytes = NULL*8

def flush():

    global buffer
    buffer.append(NULL*8)
    
    with open(device, 'rb+') as kb:
        for c in buffer:
            kb.write(c.encode())
        buffer = []

##    for c in buffer:
##        #os.system("echo -ne \"" + c + "\" > /dev/hidg0")
##        print(c.encode())
##    buffer = []

print()
print("Keyshell for Raspberry Pi Zero")
print("Press CTRL-C to quit")
print()
print("Press enter on an empty line to switch between act and type mode")
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
            if not speed:
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
            if not speed:
                flush()
    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit()
