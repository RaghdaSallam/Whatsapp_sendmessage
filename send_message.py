
import time
import pywhatkit
import pyautogui
from pynput.keyboard import Key ,Controller

keyboard =Controller()

def send_whatsapp_message(msg: str):
    try:
        pywhatkit.sendwhatmsg_instantly(phone_no="+01281102524",message=msg,tab_close=False)
        time.sleep(20)
        pyautogui.click()
        time.sleep(5)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print("Message sent!")
        
    except Exception as e:
        print(str(e))


if __name__== "__main__":
    send_whatsapp_message(msg="Text message from a Python Script!")        
    