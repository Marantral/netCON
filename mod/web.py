import concurrent.futures
import importlib
from importlib import util
import os
import subprocess


spec = importlib.util.find_spec('.subserv', package='lib')
m = spec.loader.load_module()

def dirb(http_hosts, hosts):


    dirbfile = hosts + "_dirb_scan.txt"

    print(m.bcolors.GREEN + "\n\t[*]" + m.bcolors.ENDC + "\tDoing a dirb scan on --- " + http_hosts)
    dirb = "dirb " + http_hosts +" -o ./ScanningResults/" + dirbfile
    subprocess.call(dirb, shell=True)

def nikto(hosts):


    niktofile = hosts + "_nikto_scan.html"

    print(m.bcolors.GREEN + "\n\t[*]" + m.bcolors.ENDC + "\tDoing a Nikto scan on --- " + hosts)
    nikto = "nikto -host " + hosts + " -output ./ScanningResults/" + niktofile
    subprocess.call(nikto, shell=True)


def web(http, ph_http):
    os.system("clear")
    http_hosts = []
    for f in http:
        currentPlace = f[:-1]
        http_hosts.append(currentPlace)

    hosts = []
    for f in ph_http:
        currentPlace = f[:-1]
        hosts.append(currentPlace)

    print(m.bcolors.BLUE + "\t*******************************************************************" + m.bcolors.ENDC)
    print(m.bcolors.BOLD + m.bcolors.GREEN + r"""
        *******************************************************************
          _       ____________     ____________  _________
         | |     / / ____/ __ )   /_  __/  _/  |/  / ____/
         | | /| / / __/ / __  |    / /  / // /|_/ / __/   
         | |/ |/ / /___/ /_/ /    / / _/ // /  / / /___   
         |__/|__/_____/_____/    /_/ /___/_/  /_/_____/   """ + m.bcolors.ENDC)

    print(
            m.bcolors.ERROR + "\t*******************************************************************" + m.bcolors.ENDC)

    print(m.bcolors.BLUE + "\t*******************************************************************" + m.bcolors.ENDC)
    input("\a\nLets Enumerate all web pages!!\a\nPRESS ENTER TO START!!")

    with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor:
        executor.map(dirb, http_hosts, hosts, timeout=480)
        executor.map(nikto, hosts, timeout=480)

    input("\a\n\t\tWeb Enumeration is DONE. Great Job Bro!\n\t\tPRESS ENTER TO KEEP THIS TRAIN MOVING!!")
    os.system("reset")
    os.system("clear")