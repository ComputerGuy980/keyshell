# keyshell
Yet another HID keyboard gadget script, made for Raspberry Pi Zero W.

The intention of this project is to make it very easy to remotely connect (generally ssh) into your Pi Zero and encode and send groups of keystrokes to the host machine in real time.

Written in Python.

----

To use this, you need to configure your Raspi as a USB HID gadget using ConfigFS.

This tutorial, from rmedgar.com, explains how that works in detail:

https://www.rmedgar.com/blog/using-rpi-zero-as-keyboard-setup-and-device-definition

To summarize HID gadget setup: add "dwc2" and "libcomposite" lines at the end of DATA/etc/modules on your MicroSD card; also, add "dtoverlay=dwc2" to the end of BOOT/config.txt.

Once you have booted it up, run the "setupkeyboard" script to set up the keyboard (you must do this each time you boot, because it is a volatile configuration).

Now you can use keyshell.

----

How to Use:

If your HID device is located somewhere other than "/dev/hidg0", update line 27 of "keyshell.py".

Add "setupkeyboard" to /etc/rc.local so that it is run on each boot.

Run "setup" as root. This will allow you to use the "keyshell" command to start keyshell.

When you run keyshell, you will be able to enter text at the "keyshell>" prompt.

You can also press enter on an empty line to switch in and out of action mode (where you can enter action keys, as opposed to character keys.

That's it, really.

----

I'm new to GitHub, so bear with me if I set up this repo in a strange way.
