from pynput.keyboard import Key, Listener
import sys

def forward():
    return "w"
def backward():
    return "s"
def left():
    return "d"
def right():
    return "a"
def engineoff():
    sys.exit() 
def press_key(key):
    str_key = str(key)
    str_key = str_key.replace("'","")
    if str(str_key) == "w":
        forward()
    elif str(str_key) == "s":
        backward()
    elif str(str_key) == "a":
        left()
    elif str(str_key) == "d":
        right()
    elif str(str_key) == "q":
        engineoff()
        
def release_key(key):
    return "w"

with Listener(on_press = press_key, on_release = release_key) as l:
    l.join()
    
