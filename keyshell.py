#!/usr/bin/env python3

print("starting keyshell...")

import keysdec
import sys
#from time import sleep

NULL = chr(0)

device = "/dev/hidg0"
inputfile = None

hidbytes = NULL*8
buffer = []

lastKey = None

mode = 0
speed = False

lastFlag = None

for arg in sys.argv[1:]: # discards name of program, sys.argv[0]
    if arg[0] == "-": # flag
        if lastFlag != "d" and lastFlag != "i":
            if arg[1] == "f": # fast mode - less accurate...
                speed = True
                print("speed mode on with -f flag")
            elif arg[1] == "d": # select different
                lastFlag = "d"
                continue
            elif arg[1] == "i":
                lastFlag = "i"
                continue
            else:
                print("error: unrecognized flag: " + str(arg))
                sys.exit(1)
        elif lastFlag == "d":
            print("error: no value given after -d flag")
            sys.exit(1)
        elif lastFlag == "i":
            print("error: no value given after -i flag")
            sys.exit(1)
        else:
            print("error: if you\'re seeing this, then the program has reached a presumably unreachable point; please report this bug on https://github.com/ComputerGuy980/keyshell")
            sys.exit(1)
    else:
        if lastFlag == "d":
            device = arg
            lastFlag = None
            print("selected new device: " + str(device))
        elif lastFlag == "i":
            mode = 2
            inputfile = arg
            lastFlag = None
            print("reading from file: " + str(inputfile))
        else:
            print("error: unrecognized argument: " + str(arg))
            sys.exit(1)

if lastFlag == "d":
    print("error: no value given after -d flag")
    sys.exit(1)
elif lastFlag == "i":
    print("error: no value given after -i flag")
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
    
if speed:
    def flush():
        nullcode = NULL*8
        
        with open(device, 'rb+') as kb:
            kb.write(nullcode.encode())
        #print(nullcode.encode())
else:
    def flush():

        global buffer
        buffer.append(NULL*8)
        
        with open(device, 'rb+') as kb:
            for c in buffer:
                kb.write(c.encode())
            buffer = []

##        for c in buffer:
##            #os.system("echo -ne \"" + c + "\" > /dev/hidg0")
##            print(c.encode())
##        buffer = []

if mode == 0 or mode == 1:
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
            flush()
        elif mode == 1:
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
        elif mode == 2:
            with open(inputfile,'r') as ip:
                for current in ip.read().strip():
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
            print("done.")
            sys.exit(0)
            
    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit()
