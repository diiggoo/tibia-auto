import threading
import pynput
import pyautogui
import random

from vida_mana import manager_supplies

pyautogui.useImageNotFoundException(False)

FULL_DEFENSIVE_HOTKEY = '-'
FULL_OFFENSIVE_HOTKEY = '='
USE_RING_HOTKEY = 'F10'
EAT_FOOD_HOTKEY = 'F12'
list_hotkey_before_rotation = [FULL_OFFENSIVE_HOTKEY, USE_RING_HOTKEY]
list_hotkey_after_rotation = [FULL_DEFENSIVE_HOTKEY, USE_RING_HOTKEY]

LIST_POSITION_LOOT = [
    (716, 407),
    (716, 407),
    (716, 407),
    (716, 407),
    (716, 407),
    (716, 407),
    (716, 407),
    (716, 407),
    (716, 407),
]


LIST_HOTKEY_ATTACKS = [
    {"hotkey":'F8', "delay": 0.5},
    {"hotkey":'F4', "delay": 1.5},
    {"hotkey":'F5', "delay": 1.5},
    {"hotkey":'F6', "delay": 1.5},
    ]

REGION_BATTLE = (1571, 25, 155, 34)

def rotate_skills():
    while not event_rotate_skills.is_set(): # pylint: disable=E0601
        for attack in LIST_HOTKEY_ATTACKS:
            if event_rotate_skills.is_set():
                return
            if pyautogui.locateOnScreen('battle.png', confidence=0.8, region=REGION_BATTLE):
                continue
            print('Executando: ', attack['hotkey'])
            pyautogui.press('space')
            pyautogui.press(attack["hotkey"])
            pyautogui.sleep(attack["delay"])


def execute_hotkey(hotkey):
    pyautogui.press(hotkey)

def get_loot():
    random.shuffle(LIST_POSITION_LOOT)
    pyautogui.PAUSE = 0.045
    for position in LIST_POSITION_LOOT:
        pyautogui.moveTo(position)
        pyautogui.click(button="right")
    pyautogui.PAUSE = 0.1

running = False
def key_code(key):
    global running
    global th_rotate_skills, event_rotate_skills, th_supplies, event_supplies
    if key == pynput.keyboard.Key.delete:
        print("Bot encerrado!")
        return False
    if hasattr(key, 'char') and key.char == 'f':
        if running == False:
            running = True
            global th_rotate_skills, event_rotate_skills, th_supplies, event_supplies
            event_supplies = threading.Event()
            th_supplies = threading.Thread(target=manager_supplies, args=(event_supplies, ))
            event_rotate_skills = threading.Event()
            th_rotate_skills = threading.Thread(target=rotate_skills)
            print('Iniciando rotação de skills')
            for hotkey in list_hotkey_before_rotation:
                execute_hotkey(hotkey)
            th_rotate_skills.start()
            th_supplies.start()

        else:
            running = False
            event_rotate_skills.set()
            event_supplies.set()
            th_rotate_skills.join()
            th_supplies.join()
            print('Parando rotação de skills')
            for hotkey in list_hotkey_after_rotation:
                execute_hotkey(hotkey)

    if hasattr(key, 'char') and key.char == 'r':
        print('Coletando loot')
        get_loot()
        execute_hotkey(EAT_FOOD_HOTKEY)

with pynput.keyboard.Listener(on_press=key_code) as listener:
    listener.join()
