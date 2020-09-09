#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests, os, sys
from datetime import datetime

VERBOSE  = True
DATAPATH = os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + ".." + os.sep + "data_SH" + os.sep
DATE_STR = datetime.fromtimestamp(datetime.now().timestamp()).strftime('%Y-%m-%d')
FILENAME = ["SH_Alter_{}.csv".format(DATE_STR), "SH_Kreise_{}.csv".format(DATE_STR), "SH_Verlauf_{}.csv".format(DATE_STR) ]
FULLNAME = [ DATAPATH + FILENAME[0], DATAPATH + FILENAME[1], DATAPATH + FILENAME[2] ]
CSV_URL  = ["https://phpefi.schleswig-holstein.de/corona/data/alter.csv", "https://phpefi.schleswig-holstein.de/corona/data/kreise.csv", "https://phpefi.schleswig-holstein.de/corona/data/verlauf.csv" ]

for i in range(0, 3):

    if os.path.isfile(FULLNAME[i]):
    
        if VERBOSE:
            print("The file '{}' exists already.".format(FILENAME[i]))
            
        sys.exit(0)
        
    else:
        
        if VERBOSE:
            print("The file '{}' does not exist.".format(FILENAME[i]))
            
        headers = { 'Pragma': 'no-cache', 'Cache-Control': 'no-cache' }
        
        r = requests.get(CSV_URL[i], headers=headers, allow_redirects=True, timeout=5.0)
        if r.status_code != 200:
            print("Download failed!")
            sys.exit(1)
            
        with open(FULLNAME[i], 'wb') as df:
            df.write(r.content)
            df.close()        
