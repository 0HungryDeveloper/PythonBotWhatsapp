import pyautogui as bot
import webbrowser as brave
import time
import random as r

CODE = "+521"

URL = "https://web.whatsapp.com/send?phone="


def get_phone():
    phone = input("   >Phone: ")
    return phone

def get_message():
    message = input("   >Message: ")
    return message

def showOptions():
    options = [
        "   1. 10 mensajes",
        "   2. 50 mensajes",
        "   3. 100 mensajes",
        "   4. 200 mensajes",
        "   5. 500 mensajes",
        "   6. aleatorio"
    ]

    for o in options:
        print(o)

    option = input("    > ")
    
    return option

def get_amount_of_messages(option):
    position = int(option) - 1
    random_amount_of_messages = r.randint(1,10000)
    amount = [
        10,
        50,
        100,
        200,
        500,
        random_amount_of_messages 
    ]
    return amount[position]
    

def open_browser(phone):
    brave.open(URL+CODE+phone)
    time.sleep(3000)


def bot_in_action(amout_of_messages,message):
    for i in range(1,amout_of_messages):
        bot.write(message)
        bot.press("enter")
    

if __name__ == '__main__':
    phone = get_phone()
    message = get_message()
    option = showOptions()
    open_browser(phone)
    amount_of_messages = get_amount_of_messages(option)
    bot_in_action(amount_of_messages, message)
    