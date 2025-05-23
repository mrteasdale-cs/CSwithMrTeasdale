import keyboard
from pynput.keyboard import Key, Listener

message = ''
def get_keypress(key):
    print(f"You pressed the {key} key.")

def get_keyrelease(key):
    message = ''
    if key == Key.esc:
        return False
    if key == Key.delete:
        message = message[-1]
    else:
        message += message

def write(keys):
    with open('log.txt', 'a') as f:
        for key in keys:
            f.write(key)

with Listener(on_press=get_keypress, on_release=get_keyrelease) as listener:
    listener.join()
