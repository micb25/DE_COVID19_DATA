#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests, os, sys
from datetime import datetime

VERBOSE  = True
DATAPATH = os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + ".." + os.sep + "data_HE" + os.sep
DATE_STR = datetime.fromtimestamp(datetime.now().timestamp()).strftime('%Y-%m-%d')
DATE_SHR = datetime.fromtimestamp(datetime.now().timestamp()).strftime('%Y_%m_%d')
FILENAME = "HE_{}.pdf".format(DATE_STR)
FULLNAME = DATAPATH + FILENAME
CSV_URL  = "https://soziales.hessen.de/sites/default/files/media/{}_bulletin_coronavirus.pdf".format(DATE_SHR)

if os.path.isfile(FULLNAME):

    if VERBOSE:
        print("The file '{}' exists already.".format(FILENAME))
        
    sys.exit(0)
    
else:
    
    if VERBOSE:
        print("The file '{}' does not exist.".format(FILENAME))
        
    headers = { 'Pragma': 'no-cache', 'Cache-Control': 'no-cache', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'de,en-US;q=0.7,en;q=0.3' }
    
    r = requests.get(CSV_URL, headers=headers, allow_redirects=True, stream=True, timeout=5.0)
    if r.status_code != 200:
        print("Download failed!")
        sys.exit(1)
        
    with open(FULLNAME, 'wb') as df:
        df.write(r.content)
        df.close()        
