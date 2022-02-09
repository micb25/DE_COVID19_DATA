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
CSV_URL1 = "https://www.baden-wuerttemberg.de/fileadmin/redaktion/dateien/PDF/Coronainfos/Corona_2022/{}_LGA_COVID19-Tagesbericht.pdf".format(DATE_SHR)
CSV_URL2 = "https://www.gesundheitsamt-bw.de/fileadmin/LGA/_DocumentLibraries/SiteCollectionDocuments/05_Service/LageberichtCOVID19/{}_LGA_COVID19-Tagesbericht.pdf".format(DATE_STR)

CSV_URLS = [CSV_URL1, CSV_URL2]

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
