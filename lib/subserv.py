#! /usr/bin/env python3

## File That has all of the common services


import atexit
import readline
import os
import nmap


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
