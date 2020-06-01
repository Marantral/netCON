#! /usr/bin/env python3
import errno
import subprocess
import importlib
from importlib import util
import os
import concurrent.futures


spec = importlib.util.find_spec('.subserv', package='lib')
m = spec.loader.load_module()

spec2 = importlib.util.find_spec('.nmap2', package='mod')
scan = spec2.loader.load_module()

spec3 = importlib.util.find_spec('.web', package='mod')
web = spec3.loader.load_module()

def xmlconsole(xip):


    sedcmd = "sed -n \'/<host /,/<\\/host>/p;/<\\/host>/q\' " + "./ScanningResults/" + project + "/XMLout/" + xip + "_full_scan.xml >>./ScanningResults/" + project + "/XMLout/" + "full.xml"
    subprocess.call(sedcmd, shell=True)


def main():
    global project
    print(m.bcolors.BOLD + m.bcolors.BLUE + """
                                           :####:   .####.   ###   ## 
                                 ##        ######   ######   ###   ## 
                                 ##      :##:  .#  :##  ##:  ###:  ## 
           ##.####    .####:   #######   ##        ##:  :##  ####  ## 
           #######   .######:  #######   ##.       ##    ##  ##:#: ## 
           ###  :##  ##:  :##    ##      ##        ##    ##  ## ## ## 
           ##    ##  ########    ##      ##        ##    ##  ## ## ## 
           ##    ##  ########    ##      ##.       ##    ##  ## :#:## 
           ##    ##  ##          ##      ##        ##:  :##  ##  #### 
           ##    ##  ###.  :#    ##.     :##:  .#  :##  ##:  ##  :### 
           ##    ##  .#######    #####     ######   ######   ##   ### 
           ##    ##   .#####:    .####     :####:   .####.   ##   ### 

""" + m.bcolors.ENDC)

    print(m.bcolors.GREEN + """
                    _____             __         __  ___      
                   / ___/______ ___ _/ /____ ___/ / / _ )__ __
                  / /__/ __/ -_) _ `/ __/ -_) _  / / _  / // /
                  \___/_/  \__/\_,_/\__/\__/\_,_/ /____/\_, / 
                                                       /___/  
             __  ___                   __           __  ________      
            /  |/  /__ ________ ____  / /________ _/ / /_  __/ /  ___ 
           / /|_/ / _ `/ __/ _ `/ _ \/ __/ __/ _ `/ /   / / / _ \/ -_)
          /_/  /_/\_,_/_/  \_,_/_//_/\__/_/  \_,_/_/   /_/ /_//_/\__/ 

                        __  ___          __           ____
                       /  |/  /__ ____  / /________  / / /
                      / /|_/ / _ `/ _ \/ __/ __/ _ \/ / / 
                     /_/  /_/\_,_/_//_/\__/_/  \___/_/_/  

""" + m.bcolors.ENDC)

    print("\n\n\tThanks for using this tool. First things first all files and reports will be stored in " + m.targetfolder)
    project = input("\n\tWhat is the name of this project?: ")
    projectfolder = m.targetfolder + project + "/"
    xmlfolder: object = projectfolder + "XMLout/"
    txtfolder = projectfolder + "TXTout/"
    dirbfolder = projectfolder + "DIRBout/"
    niktofolder = projectfolder + "NIKTOout"

    try:
        os.makedirs(projectfolder)
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("\n\tFolder already exists!!")
    try:
        os.makedirs(xmlfolder)
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("\n\tFolder already exists!!")
    try:
        os.makedirs(txtfolder)
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("\n\tFolder already exists!!")
    try:
        os.makedirs(dirbfolder)
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("\n\tFolder already exists!!")
    try:
        os.makedirs(niktofolder)
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("\n\tFolder already exists!!")

    projectfolder = m.targetfolder + project + "/"
    file1= "null"
    tree1 = input(
        "\n\n\tDo you have a networks file?(" + m.bcolors.BOLD + m.bcolors.ERROR + "Yes " + m.bcolors.ENDC + "or No): ") or "Yes"
    if tree1 == 'Yes':
        file1 = input("\n\tWhere is the file located?")
    elif tree1 == 'yes':
        file1 = input("\n\tWhere is the file located?")
    elif tree1 == 'y':
        file1 = input("\n\tWhere is the file located?")
    elif tree1 == 'YES':
        file1 = input("\n\tWhere is the file located?")
    elif tree1 == 'no':
        print(
            "\n\tPut in the networks that you want to scan in slash notation, single IP or a range of IPs. \n\tLike: "
            "'192.168.0.0/24 172.16.0.0/20 192.168.1.1 192.168.1.1-10'")
        net1 = input("\n\tPlease put in the networks that you are wanting to scan!:  ")
    elif tree1 == 'n':
        print(
            "\n\tPut in the networks that you want to scan in slash notation, single IP or a range of IPs. \n\tLike: "
            "'192.168.0.0/24 172.16.0.0/20 192.168.1.1 192.168.1.1-10'")
        net1 = input("\n\tPlease put in the networks that you are wanting to scan!:  ")
    elif tree1 == 'NO':
        print(
            "\n\tPut in the networks that you want to scan in slash notation, single IP or a range of IPs. \n\tLike: "
            "'192.168.0.0/24 172.16.0.0/20 192.168.1.1 192.168.1.1-10'")
        net1 = input("\n\tPlease put in the networks that you are wanting to scan!:  ")
    elif tree1 == 'No':
        print(
            "\n\tPut in the networks that you want to scan in slash notation, single IP or a range of IPs. \n\tLike: "
            "'192.168.0.0/24 172.16.0.0/20 192.168.1.1 192.168.1.1-10'")
        net1 = input("\n\tPlease put in the networks that you are wanting to scan!:  ")
    else:
        print("\n\tI didn't understand your input! Have a great day")
        exit()



    if file1 != "null":
        nmap_args_file = "-sn -T4 -oG " + projectfolder + ".ping_scan.txt -iL " + file1
        print("\n\n\tScanning for Up hosts!")
        m.nmap_scan.scan(arguments=nmap_args_file)
    elif net1 != "":
        nmap_args = "-sn -T4 -oG " + projectfolder + ".ping_scan.txt"
        print("\n\n\tScanning for Up hosts!")
        m.nmap_scan.scan(hosts=net1, arguments=nmap_args)
    else:
        return
    uphosts = "cat " + projectfolder + ".ping_scan.txt | grep 'Up' | cut -d ' ' -f 2 >" + projectfolder + project + "-Uphosts.txt"
    subprocess.call(uphosts, shell=True)
    print("\n\n\tAll up hosts are in " + m.bcolors.BOLD + m.bcolors.ERROR + projectfolder + project + "-Uphosts.txt!"+ m.bcolors.ENDC  + "\n\tYou should upload that into a vulnerability scanner.")

    hosts = open(projectfolder + project + "-Uphosts.txt", "r")
    input("\n\tPress enter to continue!")

    scan.nmap(hosts)

    mvtxt = "mv " + m.targetfolder + "*.txt " + txtfolder
    mvxml = "mv " + m.targetfolder + "*.xml " + xmlfolder

    subprocess.call(mvtxt, shell=True)
    subprocess.call(mvxml, shell=True)

    fullxml = """<?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE nmaprun>
    <?xml-stylesheet href="file:///usr/bin/../share/nmap/nmap.xsl" type="text/xsl"?>
    <nmaprun scanner="nmap" args="nmap">
    <scaninfo type="connect" protocol="tcp"/>
    <verbose />
    <debugging />
    """
    full_xml = open(xmlfolder + "full.xml", "w")
    full_xml.write(fullxml)
    full_xml.close()
    xip = []
    for f in hosts:
        currentPlace = f[:-1]
        xip.append(currentPlace)

    with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor:
        executor.map(xmlconsole, xip)

    exml1 = "'<runstats><finished/><hosts/>'"
    exml2 = "'</runstats>'"
    exml3 = "'</nmaprun>'"

    xmlcmd1 = "echo " + exml1 + " >>" + xmlfolder + "full.xml"
    xmlcmd2 = "echo " + exml2 + " >>" + xmlfolder + "full.xml"
    xmlcmd3 = "echo " + exml3 + " >>" + xmlfolder + "full.xml"

    subprocess.call(xmlcmd1, shell=True)
    subprocess.call(xmlcmd2, shell=True)
    subprocess.call(xmlcmd3, shell=True)

    smb_relay = "egrep 'message_signing: disabled' ./ScanningResults/" + project + "/TXTout/*_full_scan.txt -r | cut -d '/' -f 5 | cut -d '_' -f 1 >" + projectfolder + "smbSigning.txt"
    subprocess.call(smb_relay, shell=True)

    if os.stat(projectfolder + "smbSigning.txt").st_size == 0:
        pass
    else:
        print(m.bcolors.BOLD+ m.bcolors.ERROR +'\n\tSMB Signing is Disabled in this environment.'+ m.bcolors.ENDC +'I would try some SMB Relaying\n\tEdit the responder.conf file and disable SMB and HTTP.\n\tIn responder tools there is MultiRelay!\n\tissue: "./MultiRelay.py -t X.X.X.X -u ALL" After you start responder')
        input("\n\n\tThese are the hosts that have Signing Disabled!\n\t" + projectfolder + "smbSigning.txt\n\n\t Press Enter to keep going!")

    htmlcreate = "xsltproc " + xmlfolder + "full.xml -o " + projectfolder + "NMAP_Results.html"
    subprocess.call(htmlcreate, shell=True)
    print("\n\tNMAP HTML Created!  It is located in: " + m.bcolors.BOLD + m.bcolors.ERROR + projectfolder + "NMAP_Results.html" + m.bcolors.ENDC)
    input("\n\tPress Enter to Keep going!!")

    non_ssl = "egrep \'http\' ./ScanningResults/" + project + r"/TXTout/*_full_scan.txt -r | grep 'open' | grep -v 'ssl' | cut -d '/' -f 5 | sed \'s/_full_scan.txt//'| sed 's/^/https:\/\//' >>" + projectfolder + "httphosts.txt"
    ssl = "egrep 'http' ./ScanningResults/" + project + r"/TXTout/*_full_scan.txt -r | grep 'open' | grep  'ssl' | cut -d '/' -f 5 | sed 's/_full_scan.txt//'| sed 's/^/https:\/\//' >>" + projectfolder + "httphosts.txt"
    ipport = "cat " +projectfolder + "httphosts.txt | cut -d '/' -f 3 >" + projectfolder +"http_ports_ips.txt"
    subprocess.call(non_ssl, shell=True)
    subprocess.call(ssl, shell=True)
    subprocess.call(ipport, shell=True)

    http = open(projectfolder + "httphosts.txt", "r")
    ph_http = open(projectfolder + "http_ports_ips.txt", "r")

    web.web(http, ph_http)

    mvdirb = "mv " + m.targetfolder + "*.txt " + dirbfolder
    mvhtml = "mv " + m.targetfolder + "*.html " + niktofolder

    subprocess.call(mvdirb, shell=True)
    subprocess.call(mvhtml, shell=True)

    dirbup = "egrep \'\\(CODE:200' ./ScanningResults/" + project + "/DIRBout/ -r |cut -d ' ' -f 2,3 >" + projectfolder + "200_Webpages.txt"
    subprocess.call(dirbup, shell=True)
    print("\n\n\tAll 200 pages are located within: " + m.bcolors.BOLD + m.bcolors.ERROR + projectfolder + "200_Webpages.txt" + m.bcolors.ENDC)
    print("\n\tThe Nikto Scan results are stored in: " + m.bcolors.BOLD + m.bcolors.ERROR + niktofolder + m.bcolors.ENDC)

    input("\n\tPress Enter to Look at your stuff!!\n\tThis is not done being built I will add to it later!")



# call main() function
if __name__ == '__main__':
    main()