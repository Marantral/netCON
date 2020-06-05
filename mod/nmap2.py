import concurrent.futures
import importlib
from importlib import util
import os
import subprocess

spec = importlib.util.find_spec('.subserv', package='lib')
m = spec.loader.load_module()

def basic(ip):

    bfilename = ip + "_basic_scan.txt"

    print(m.bcolors.GREEN + "\n\t[*]" + m.bcolors.ENDC + "\tDoing a basic TCP scan on ---" + ip)
    basic = "nmap -sS -oN ./ScanningResults/" + bfilename + " -T4 " + ip
    subprocess.call(basic, shell=True)

def full(ip):

    filename = ip + "_full_scan.txt"
    filexml = ip + "_full_scan.xml"

    print(m.bcolors.GREEN + "\n\t[*]" + m.bcolors.ENDC + "\tDoing a full TCP scan on ---" + ip)
    full = "nmap -oX  ./ScanningResults/" + filexml + " -oN ./ScanningResults/" + filename + " -T4  --max-retries 1 --host-timeout 10m -sC -sS  -A -p- " + ip
    subprocess.call(full, shell=True)
def udp(ip):

    filename = ip + "_udp_scan.txt"
    filexml = ip + "_udp_scan.xml"


    print(m.bcolors.GREEN + "\n\t[*]" + m.bcolors.ENDC + "\tDoing a UDP scan on ---" + ip)
    full = "nmap -oX  ./ScanningResults/" + filexml + " -oN ./ScanningResults/" + filename + " -T4  --max-retries 1 --host-timeout 10m -sU -A --top-ports 200  " + ip
    subprocess.call(full, shell=True)
def nmap(hosts):
    ip = []
    for f in hosts:
        currentPlace = f[:-1]
        ip.append(currentPlace)
    os.system("clear")



    print(m.bcolors.BLUE + "\t*******************************************************************" + m.bcolors.ENDC)
    print(m.bcolors.BOLD + m.bcolors.GREEN + r"""
        *******************************************************************
            _   ____  ______    ____     ___        __  _           
           / | / /  |/  /   |  / __ \   /   | _____/ /_(_)___  ____ 
          /  |/ / /|_/ / /| | / /_/ /  / /| |/ ___/ __/ / __ \/ __ \
         / /|  / /  / / ___ |/ ____/  / ___ / /__/ /_/ / /_/ / / / /
        /_/ |_/_/  /_/_/  |_/_/      /_/  |_\___/\__/_/\____/_/ /_/ """ + m.bcolors.ENDC)

    print(
            m.bcolors.ERROR + "\t*******************************************************************" + m.bcolors.ENDC)

    print(m.bcolors.BLUE + "\t*******************************************************************" + m.bcolors.ENDC)
    input("\a\nLets Enumerate this fool!!\nPRESS ENTER TO START!!")

    with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor:
        executor.map(basic, ip)
        executor.map(full, ip)
    os.system("reset")
    print(m.bcolors.BOLD + m.bcolors.ERROR + "\n\tBE CAREFUL! Doing a UDP scan on a large range could take a while!" + m.bcolors.ENDC)
    choice = input("\a\n\tDo you want to also scan UDP ports?"+ m.bcolors.BOLD + m.bcolors.ERROR + " Yes " + m.bcolors.ENDC + "or No: ") or 'Yes'
    if choice == 'Yes':
        with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor:
            executor.map(udp, ip)
    elif choice == 'YES':
        with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor:
            executor.map(udp, ip)
    elif choice == 'yes':
        with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor:
            executor.map(udp, ip)
    elif choice == 'y':
        with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor:
            executor.map(udp, ip)
    elif choice == 'Y':
        with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor:
            executor.map(udp, ip)
    else:
        pass
    input("\a\n\t\tNMAP is DONE. Great Job Bro!\n\t\tPRESS ENTER TO KEEP THIS TRAIN MOVING!!")
    os.system("reset")
    os.system("clear")