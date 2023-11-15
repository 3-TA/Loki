import os
os.system ("""/usr/local/bin/python -c 'import urllib; import ssl; ssl._create_default_https_context = ssl._create_unverified_context; import time; time.sleep (1); urllib.urlretrieve ("https://github.com/3-TA/Loki/raw/main/moantroll.mp3", "/Users/Shared/moantroll.mp3")'""")
