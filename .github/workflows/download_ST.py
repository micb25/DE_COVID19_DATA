#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests, re, os, sys
from datetime import datetime

VERBOSE  = True
DATAPATH = os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + ".." + os.sep + "data_ST" + os.sep
DATE_STR = datetime.fromtimestamp(datetime.now().timestamp()).strftime('%Y-%m-%d')
FILENAME = "ST_{}.pdf".format(DATE_STR)
FULLNAME = DATAPATH + FILENAME
HTML_URL = "https://ms.sachsen-anhalt.de/themen/gesundheit/aktuell/coronavirus/"

PDF_RE   = re.compile(r"\"(https://ms.sachsen-anhalt.de/fileadmin/Bibliothek/Politik_und_Verwaltung/MS/MS/Presse_Corona/[a-zA-Z0-9_/]*?Corona_Update[a-zA-Z0-9_/]*?.pdf)\"")

if os.path.isfile(FULLNAME):

    if VERBOSE:
        print("The file '{}' exists already.".format(FILENAME))
        
    sys.exit(0)
    
else:
    
    if VERBOSE:
        print("The file '{}' does not exist.".format(FILENAME))
        
    headers = { 'Pragma': 'no-cache', 'Cache-Control': 'no-cache' }
    
    r = requests.get(HTML_URL, headers=headers, allow_redirects=True, timeout=5.0)
    if r.status_code != 200:
        print("Download failed!")
        sys.exit(1)
        
    pre = PDF_RE.findall( r.text.replace("\n", "") )
    if len(pre) != 1:
        print("Download failed (link not found)!")
        sys.exit(1)
        
    p = requests.get(pre[0], headers=headers, allow_redirects=True, timeout=5.0)
    if p.status_code != 200:
        print("PDF Download failed!")
        sys.exit(1)
        
    with open(FULLNAME, 'wb') as df:
        df.write(p.content)
        df.close()        
