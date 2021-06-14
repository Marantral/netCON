#! /usr/bin/env python3

## File That has all of the common services


import atexit
import readline
import os
import nmap
import errno
import pathlib

nofile = "\n\tPut in the networks that you want to scan in slash notation, single IP or a range of IPs. \n\tLike: " \
         "'192.168.0.0/24 172.16.0.0/20 192.168.1.1 192.168.1.1-10' "

nmap_scan = nmap.PortScanner()

histfile = os.path.join(os.path.expanduser("~"), ".netCON_history")
try:
    readline.read_history_file(histfile)
    h_len = readline.get_current_history_length()
except FileNotFoundError:
    open(histfile, 'wb').close()
    h_len = 0

def save(prev_h_len, histfile):
    new_h_len = readline.get_current_history_length()
    readline.set_history_length(1000)
    readline.append_history_file(new_h_len - prev_h_len, histfile)
atexit.register(save, h_len, histfile)



class bcolors:
  BLUE = '\033[94m'
  GREEN = '\033[92m'
  WARNING = '\033[93m'
  WHITE = '\033[97m'
  ERROR = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'


#Install location
loc = os.getcwd()
#Results output file
targetfolder = loc + "/ScanningResults/"

def folder_create(folder):
    try:
        os.makedirs(folder)
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("\n\tFolder already exists!!")

def file_ex(file1):
    file = pathlib.Path(file1)
    if file.exists():
        pass
    else:
        print(
            bcolors.ERROR + "\a\n\t\tThere is no file: " + file1 + "\a\n\t\tFigure yourself out!\a\n\n\t\t       BYE BRO!" + bcolors.ENDC)
        exit()
