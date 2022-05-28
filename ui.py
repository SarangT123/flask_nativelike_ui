import webview
import time
import app
import os
import platform
import requests
import tkinter
from tkinter import messagebox
from tkinter.messagebox import askyesno

debug = False
admin_stopper = True


def popup_warning(msg):

    # This code is to hide the main tkinter window
    root = tkinter.Tk()
    root.withdraw()

    # Message Box
    messagebox.showwarning('Error', msg)
    # end programe
    root.destroy()


if __name__ == '__main__':
    if debug:
        popup_warning(
            'WARNING: This is a development server. Do not use it in a production deployment.\nTurn off debug mode to run the server in production.')

    if platform.system() == 'Linux' or platform.system() == 'MacOS':
        print('Running on Linux or MacOS')
        os.system('pkill flask')
        if debug:
            os.system('flask run --debugger --reload &')
        else:
            os.system('flask run &')
        x = True
        while x:
            try:
                x = requests.get('http://127.0.0.1:5000/').status_code != 200
                print(x)
            except:
                pass
            time.sleep(1)
        webview.create_window(
            'Flask boilerplate app', 'http://127.0.0.1:5000', background_color='#FFFFFF', js_api=True, frameless=False)
        webview.start()
        if debug:
            os.system('pkill flask')
        else:
            os.system('pkill flask')
        exit(0)
    elif platform.system() == 'Windows':
        os.system('taskkill /f /im flask.exe')
        if debug:
            os.system('flask run --debugger --reload &')
        else:
            os.system('flask run &')
        x = True
        while x:
            try:
                x = requests.get('http://127.0.0.1:5000/').status_code != 200
                print(x)
            except:
                pass
            time.sleep(1)
        webview.create_window(
            'Flask boilerplate app', 'http://127.0.0.1:5000', background_color='#FFFFFF', js_api=True, frameless=False)
        webview.start()
        if debug:
            os.system('taskkill /f /im flask.exe')
        else:
            os.system('taskkill /F /IM flask.exe')
        exit(0)

    else:
        popup_warning('Your system is not supported')
        exit(1)
