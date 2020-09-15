#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests, os, sys
from datetime import datetime

VERBOSE  = True
DATAPATH = os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + ".." + os.sep + "data_BW" + os.sep
DATE_STR = datetime.fromtimestamp(datetime.now().timestamp()).strftime('%Y-%m-%d')
DATE_SHR = datetime.fromtimestamp(datetime.now().timestamp()).strftime('%y%m%d')
FILENAME = "BW_{}.pdf".format(DATE_STR)
FULLNAME = DATAPATH + FILENAME
CSV_URL1 = "https://www.baden-wuerttemberg.de/fileadmin/redaktion/dateien/PDF/Coronainfos/{}_COVID_Tagesbericht_LGA.pdf".format(DATE_SHR)
CSV_URL2 = "https://www.baden-wuerttemberg.de/fileadmin/redaktion/dateien/PDF/Coronainfos/{}_COVID_Lagebericht_LGA.pdf".format(DATE_SHR)
CSV_URL3 = "https://www.baden-wuerttemberg.de/fileadmin/redaktion/m-sm/intern/downloads/Downloads_Gesundheitsschutz/{}_COVID_Tagesbericht_LGA.pdf".format(DATE_SHR)
CSV_URL4 = "https://www.baden-wuerttemberg.de/fileadmin/redaktion/m-sm/intern/downloads/Downloads_Gesundheitsschutz/{}_COVID_Lagebericht_LGA.pdf".format(DATE_SHR)

CSV_URLS = [CSV_URL1, CSV_URL2, CSV_URL3, CSV_URL4]

if os.path.isfile(FULLNAME):

    if VERBOSE:
        print("The file '{}' exists already.".format(FILENAME))
        
    sys.exit(0)
    
else:
    
    if VERBOSE:
        print("The file '{}' does not exist.".format(FILENAME))
        
    headers = { 'Pragma': 'no-cache', 'Cache-Control': 'no-cache' }
    
    for CSV_URL in CSV_URLS:
        
        r = requests.get(CSV_URL, headers=headers, allow_redirects=True, timeout=5.0)
        if r.status_code == 200:
            
            with open(FULLNAME, 'wb') as df:
                df.write(r.content)
                df.close()        
                
            sys.exit(0)
    
    print("Download failed!")
    sys.exit(1)
