# Gamepad-buttons
 HID game controller with 6 buttons. Built on the basis of the "Seeed Studio XIAO SAMD21" microcontroller and programmed in CircuitPython. Visible to the system as Game Controller with 6 buttons.

![This is an image](/images/game_controllers.png)
![This is an image](/images/CP_HID_prop.png)

The code was created for the needs of additional buttons mounted on the VR headset - HP Reverb G2 made according to the instructions.

## Requirements for the microcontroller
1. Installing CircuitPython on the microcontroller according the [instruction](https://wiki.seeedstudio.com/Seeeduino-XIAO-CircuitPython/).
2. Add CircuitPython library files. Can be download from the [official libraries](https://circuitpython.org/libraries) on the CircuitPython website. Required libriaries are:
    - /adafruit_bus_device
    - /adafruit_hid
    - adafruit_debouncer.mpy
    - adafruit_ticks.mpy
    - simpleio.mpy

    Copy the files onto the CIRCUITPY drive into the /lib directory.

## Code
Copy the files: *boot.py*, *hid_gamepad.py* and *code.py* onto the CIRCUITPY directly. Reconnect device and should works.