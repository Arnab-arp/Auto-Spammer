import pyautogui as auto
from pyautogui import FailSafeException
import json
import time
import random as rd

def Get_Prompts(json_file: str) -> list:
    """
    :param json_file: Absolute Path of the Json File
    :return list: Return a list of Image Generation Prompts
    Description:
    This Function takes in a json file containing the prompts for the image generation.
    Executing this Function will return a list containing only prompts.
    """
    with open(json_file, 'r') as prompts:
        data = json.load(prompts)
    return list(data.values())

def Get_Randomized_Prompts(prompts: list) -> str:
    """
    :param prompts: List containing only the prompts
    :return str: Returns a random string from the prompts
    Description:
    This Function takes in a list containing the prompts for the image generation.
    Executing this Function will return a single random prompt from the list.
    """

    rd.shuffle(prompts)
    return rd.choice(prompts)

def Start_Spammer(img_prompts, write_delay=0.05, time_delay=0.01) -> None:
    """
    :param img_prompts:  Takes the prompts list containing all the image generation prompts
    :param write_delay: Sets the writing speed of the spammer in seconds
    :param time_delay: Sets the sleep time for executing keyboard instruction.
    :return None:
    Description:
    This Function takes in absolute json file path, writing delay (default 0.05), and time delay (default 0.01).
    Writes the prompt using pyautogui library on any writable space.

    Exception case:
    If the mouse pointer is pointed at the corner of the screen,
    it will raise a FailSafeException, effectively ending the program.
    """
    reset_counter = 0
    iterator = 0
    try:
        while iterator <= 100:
            if reset_counter == 4:
                reset_counter = 0
                delay = 61
                print("*" * 30)
                print(f'Total Prompts Written :: {iterator}\nWaiting for {delay} seconds.')
                print("*" * 30)
                time.sleep(delay)

            rd_prompt = Get_Randomized_Prompts(img_prompts).capitalize()
            if len(rd_prompt) > 1000:
                rd_prompt = rd_prompt[:1000]
            print(f"Writing :: {rd_prompt}")

            auto.write('/generate', interval=write_delay)
            time.sleep(time_delay)
            auto.press('space')
            time.sleep(time_delay)
            auto.write(rd_prompt, interval=write_delay)
            auto.press('enter')
            reset_counter += 1
            time.sleep(5)
            iterator += 1

    except FailSafeException:
        print("Quitting Spammer . . .")
        quit()

if __name__ == '__main__':
    ABS_PATH = 'Img_Gen_Prompts.json'
    status = 0
    try:
        prompts_list = Get_Prompts(ABS_PATH)
        status = 1
        print(f"Json File Path :: {ABS_PATH}\nLoading Status :: {status}")
    except Exception as e:
        print(f"Exception Occurred While Loading the JSON file.\n  >> {e}\n  >> Loading Satus :: {status}")


    if status == 1:
        print("Please Click On The Message Area.")
        time.sleep(3)
        print("Message Spammer Starting in ::", end=' ')

        for i in range(-5, 1, 1):
            print(abs(i), end=' ', flush=True)
            time.sleep(1)
        print('\n')

        Start_Spammer(img_prompts=prompts_list)

    
