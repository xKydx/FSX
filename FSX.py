#!/usr/bin/env python

import glob
import os
from sys import argv
from termcolor import colored

lookin = argv

prompt1 = '.:|'

running = True

while running:
    print ("")
    print ("")
    print ("Please enter your search start point. eg: / or /home/yourname")
    print("")
    print("")
    lookin = raw_input (prompt1)
#	User inputs starting directory location.
    print("")
    print("")
    print ("Enter file name")
    search = raw_input(prompt1)
    print("")
    print("")
#	User inputs file name.
    print colored("Depending on your search critiria,This could take a few min", "red")
    print""
    print""
#			This part was confusing at first,
#		Tell walk to look in dir's and files starting at /. update: user chooses what dir, / is now lookin argv
#		look for files, dir's and sub dirs names from user input, then display them on srceen.
    for dirname, dirnames, filenames in os.walk(lookin):
        for i in glob.glob(dirname+'/'+search+'*'):
            print colored (i,"blue")

    print ("Enter Y to continue or N to quit")
    restart = raw_input(prompt2)
    if 'y' in restart:#if you enter "y" program restarts
        running
    else:
        print colored("FSX terminated", "red")
        running = False
        #if you enter anything else program closes.
