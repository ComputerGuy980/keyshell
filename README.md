# keyshell
An HID keyboard gadget script, made for injecting text in real time with a Raspberry Pi Zero W.

The intention of this project is to make it very easy to remotely connect (generally <a href="https://www.raspberrypi.org/documentation/remote-access/ssh/README.md">ssh</a>) into your Pi Zero and encode and send groups of keystrokes to the host machine in real time.

Written in Python.

----

To use this, you need to configure your Raspi as a USB HID gadget using ConfigFS.

To summarize HID gadget setup: add "dwc2" and "libcomposite" lines at the end of DATA/etc/modules on your MicroSD card; also, add "dtoverlay=dwc2" to the end of BOOT/config.txt.


<a href="https://www.rmedgar.com/blog/using-rpi-zero-as-keyboard-setup-and-device-definition">This tutorial</a>, from rmedgar.com, explains how that works in detail.

----

**How to Setup:**

    git clone https://github.com/computerguy980/keyshell
    
    cd /path/to/files # e.g. /home/pi/keyshell
    
    sudo bash setup
    
    sudo setupkeyboard
    
You should add "setupkeyboard" to <a href="https://www.raspberrypi.org/documentation/linux/usage/rc-local.md">/etc/rc.local</a> so that it is run on each boot.

If you are using the pi as, say, a <a href = "https://www.raspberrypi.org/documentation/configuration/wireless/access-point.md" > WiFi Access Point</a> to control it outside your home network (I do) then you cannot use "git clone". Therefore, you have to copy the files to /home/pi on the MicroSD card from another computer, or use <a href="https://www.raspberrypi.org/documentation/remote-access/ssh/scp.md">scp</a> and the like to add them while connected to the Pi.

**How to Use:**

    keyshell

When you run keyshell, you will be able to enter text at the "keyshell>" prompt.

You can also press enter on an empty line to switch in and out of action mode (where you can enter modifier keys, as opposed to character keys.

If your HID device is located somewhere other than "/dev/hidg0", use the -d flag, explained below under "Command Line Arguments"

<b>Command Line Arguments (e.g. "keyshell [args]"):</b>
  
  -d, device - <i>selects a different virtual HID device</i>
  
      ex: "keyshell -d /dev/hidg1"
  
  -f, fast - <i>encodes and outputs without saving to a buffer; faster, but timing problems will be more likely</i>
  
      ex: "keyshell -f"
      
  -i, input - <i>outputs text read from a file</i>
  
      ex: "keyshell -i text.txt"
