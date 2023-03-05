import time
import board
import digitalio
import analogio
from digitalio import DigitalInOut, Direction, Pull
import usb_hid

from hid_gamepad import Gamepad

gp = Gamepad(usb_hid.devices)

button_pins = (board.D2, board.D1, board.D0, board.D4, board.D5, board.D6)

# Map the buttons to button numbers on the Gamepad.
# gamepad_buttons[i] will send that button number when buttons[i]
# is pushed.
gamepad_buttons = (1, 2, 3, 4, 5, 6)

buttons = [digitalio.DigitalInOut(pin) for pin in button_pins]
for button in buttons:
    button.direction = Direction.INPUT
    button.pull = Pull.UP

while True:
    # Buttons are grounded when pressed (.value = False)
    for i, button in enumerate(buttons):
        gamepad_button_num = gamepad_buttons[i]
        if button.value:
            gp.release_buttons(gamepad_button_num)
            print(" release", gamepad_button_num, end="")
        else:
            gp.press_buttons(gamepad_button_num)
            print(" press", gamepad_button_num, end="")
    time.sleep(0.2)  # sleep for debounce