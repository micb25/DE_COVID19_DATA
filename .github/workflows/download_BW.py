#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests, os, sys
from datetime import datetime

VERBOSE  = True
DATAPATH = os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + ".." + os.sep + "data_BW" + os.sep
STR_YEAR = datetime.fromtimestamp(datetime.now().timestamp()).strftime('%Y')
DATE_STR = datetime.fromtimestamp(datetime.now().timestamp()).strftime('%Y-%m-%d')
DATE_SHR = datetime.fromtimestamp(datetime.now().timestamp()).strftime('%y%m%d')
FILENAME = "BW_{}.pdf".format(DATE_STR)
FULLNAME = DATAPATH + FILENAME
PDF_URLS = [
    "https://www.baden-wuerttemberg.de/fileadmin/redaktion/dateien/PDF/Coronainfos/Corona_{}/{}_LGA_COVID19-Tagesbericht.pdf".format(STR_YEAR, DATE_SHR),
    "https://www.baden-wuerttemberg.de/fileadmin/redaktion/dateien/PDF/Coronainfos/Corona_{}/{}_LGA_COVID19-Lagebericht.pdf".format(STR_YEAR, DATE_SHR),
    "https://www.baden-wuerttemberg.de/fileadmin/redaktion/dateien/PDF/Coronainfos/Corona_{}/{}_LGA_COVID19-Inzidenzbericht.pdf".format(STR_YEAR, DATE_SHR),
    "https://www.gesundheitsamt-bw.de/fileadmin/LGA/_DocumentLibraries/SiteCollectionDocuments/05_Service/LageberichtCOVID19/{}_LGA_COVID19-Tagesbericht.pdf".format(DATE_STR),
    "https://www.gesundheitsamt-bw.de/fileadmin/LGA/_DocumentLibraries/SiteCollectionDocuments/05_Service/LageberichtCOVID19/{}_LGA_COVID19-Lagebericht.pdf".format(DATE_STR),
    "https://www.gesundheitsamt-bw.de/fileadmin/LGA/_DocumentLibraries/SiteCollectionDocuments/05_Service/LageberichtCOVID19/{}_LGA_COVID19-Inzidenzbericht.pdf".format(DATE_STR),
    "https://www.baden-wuerttemberg.de/fileadmin/redaktion/dateien/PDF/Coronainfos/{}_COVID_Tagesbericht_LGA.pdf".format(DATE_SHR),
    "https://www.baden-wuerttemberg.de/fileadmin/redaktion/dateien/PDF/Coronainfos/{}_COVID_Inzidenzbericht-Wochenende.pdf".format(DATE_SHR),
    "https://www.baden-wuerttemberg.de/fileadmin/redaktion/dateien/PDF/Coronainfos/{}_COVID_Tagesbericht.pdf".format(DATE_SHR),
    "https://www.baden-wuerttemberg.de/fileadmin/redaktion/dateien/PDF/Coronainfos/{}COVID_Inzidenzbericht-Wochenende.pdf".format(DATE_SHR),
    "https://www.baden-wuerttemberg.de/fileadmin/redaktion/dateien/PDF/Coronainfos/{}_COVID_Inzidenzbericht_Wochenende_LGA.pdf".format(DATE_SHR),
    "https://www.baden-wuerttemberg.de/fileadmin/redaktion/dateien/PDF/Coronainfos/{}_COVID_Inzidenzbericht_Wochenende_LGA_01.pdf".format(DATE_SHR),
    "https://www.baden-wuerttemberg.de/fileadmin/redaktion/dateien/PDF/Coronainfos/{}_COVID_Lagebericht_LGA_01.pdf".format(DATE_SHR),
    "https://www.baden-wuerttemberg.de/fileadmin/redaktion/dateien/PDF/Coronainfos/{}_COVID_Inzidenzbericht-Wochenende_LGA.pdf".format(DATE_SHR),
    "https://www.baden-wuerttemberg.de/fileadmin/redaktion/dateien/PDF/Coronainfos/{}_COVID_Inzidenzbericht_LGA.pdf".format(DATE_SHR),
    "https://www.baden-wuerttemberg.de/fileadmin/redaktion/dateien/PDF/Coronainfos/{}_COVID_Tagesbericht_LGA_01.pdf".format(DATE_SHR),
    "https://www.baden-wuerttemberg.de/fileadmin/redaktion/dateien/PDF/Coronainfos/{}_COVID_Inzidenzbericht-Feiertag.pdf".format(DATE_SHR),
    "https://www.baden-wuerttemberg.de/fileadmin/redaktion/dateien/PDF/Coronainfos/{}_COVID_Lagebericht.pdf".format(DATE_SHR),
    "https://www.baden-wuerttemberg.de/fileadmin/redaktion/dateien/PDF/Coronainfos/{}_COVID_Inzidenzbericht_Wochenende.pdf".format(DATE_SHR),
    "https://www.baden-wuerttemberg.de/fileadmin/redaktion/dateien/PDF/Coronainfos/{}_COVID_Tagebericht_LGA.pdf".format(DATE_SHR),
    "https://www.baden-wuerttemberg.de/fileadmin/redaktion/dateien/PDF/Coronainfos/{}_COVID_Tagesbericht_LGA.pdf".format(DATE_SHR),
    "https://www.baden-wuerttemberg.de/fileadmin/redaktion/dateien/PDF/Coronainfos/{}_COVID_Tagesberich_LGA.pdf".format(DATE_SHR),
    "https://www.baden-wuerttemberg.de/fileadmin/redaktion/dateien/PDF/Coronainfos/{}_COVID_Lagebericht_01.pdf".format(DATE_SHR),
    "https://www.baden-wuerttemberg.de/fileadmin/redaktion/dateien/PDF/Coronainfos/{}_COVID_Tagesbericht_LGA_V2.pdf".format(DATE_SHR),
    "https://www.baden-wuerttemberg.de/fileadmin/redaktion/dateien/PDF/{}_COVID_Inzidenzbericht_Wochenende.pdf".format(DATE_SHR),
]

if os.path.isfile(FULLNAME):

    if VERBOSE:
        print("The file '{}' exists already.".format(FILENAME))
        
    sys.exit(0)
    
else:
    
    if VERBOSE:
        print("The file '{}' does not exist.".format(FILENAME))
        
    headers = { 'Pragma': 'no-cache', 'Cache-Control': 'no-cache' }
    
    for PDF_URL in PDF_URLS:
        
        r = requests.get(PDF_URL, headers=headers, allow_redirects=True, timeout=5.0)
        if r.status_code == 200:
            
            with open(FULLNAME, 'wb') as df:
                df.write(r.content)
                df.close()        
                
            sys.exit(0)
    
    print("Download failed!")
    sys.exit(1)
