#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests, os, sys
from datetime import datetime

VERBOSE  = True
DATAPATH = os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + ".." + os.sep + "data_SL" + os.sep
DATE_STR = datetime.fromtimestamp(datetime.now().timestamp()).strftime('%Y-%m-%d')
FILENAME = "SL_{}.html".format(DATE_STR)
FULLNAME = DATAPATH + FILENAME
CSV_URL  = "https://corona.saarland.de/DE/service/chronologie-corona/chronologie-corona_node.html"

if os.path.isfile(FULLNAME):

    if VERBOSE:
        print("The file '{}' exists already.".format(FILENAME))
        
    sys.exit(0)
    
else:
    
    if VERBOSE:
        print("The file '{}' does not exist.".format(FILENAME))
        
    headers = { 'Pragma': 'no-cache', 'Cache-Control': 'no-cache' }
    
    r = requests.get(CSV_URL, headers=headers, allow_redirects=True, timeout=5.0)
    if r.status_code != 200:
        print("Download failed!")
        sys.exit(0)
        
    with open(FULLNAME, 'wb') as df:
        df.write(r.content)
        df.close()        
