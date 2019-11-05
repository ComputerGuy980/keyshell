# keyshell
Yet another HID keyboard script, made for Raspberry Pi Zero W.

Written in Python.

----

To use this, you need to configure your Raspi as a USB HID gadget using ConfigFS.

This series of tutorials I found seem explain the concept perfectly:

https://www.rmedgar.com/blog/using-rpi-zero-as-keyboard-setup-and-device-definition

https://www.rmedgar.com/blog/using-rpi-zero-as-keyboard-report-descriptor

https://www.rmedgar.com/blog/using-rpi-zero-as-keyboard-send-reports

Follow the first two for creation of the HID device, the last one is more about the specifics of keyboard actions.

Once you've followed the instructions in the tutorials, simply run "keyshell.py" as root in the same directory as "keysdec.py".

If your HID device is located somewhere other than "/dev/hidg0", update line 27 of "keyshell.py".

When you run "keyshell.py", you should see some introductory lines and then a "keyshell>" prompt. Type at this prompt to send character keystrokes.

You can also press enter on an empty line to switch in and out of action mode (where you can enter action keys, as opposed to character keys.

That's it, really.

----

I'm new to GitHub, so bear with me if I set up this repo in a strange way.
