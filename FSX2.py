#!/usr/bin/env python
# File Search Xterm Version II
import glob
import os
from sys import argv


lookin = argv

prompt = '.:|'

running = True

while running:
    print ("")
    print ("")
    print ("Please enter your search start point. eg: / or /home/yourname")
    print("")
    print("")
    lookin = raw_input (prompt)
#	User inputs starting directory location.
    print("")
    print("")
    print ("Enter file name")
    search = raw_input(prompt)
    print("")
    print("")
#	User inputs file name.
    print("Depending on your search critiria,This could take a few min")
    print""
    print""
    for dirname, dirnames, filenames in os.walk(lookin):
        for i in glob.glob(dirname+'/'+search+'*'):
            print(i)

    print ("Enter Y to continue or N to quit")
    restart = raw_input(prompt)
    if 'y' in restart:
        running
    else:
        print("FSX terminated")
        running = False
