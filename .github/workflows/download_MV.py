#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests, re, os, sys, hashlib
from datetime import datetime

def was_file_downloaded(sha256array, contents):
    if contents != False:
        new_data_sha256sum = hashlib.sha256(contents).hexdigest()
        for (filename, sha256sum) in sha256array:
            if sha256sum == new_data_sha256sum:
                return True
    return False

VERBOSE  = True
DATAPATH = os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + ".." + os.sep + "data_MV" + os.sep
DATE_STR = datetime.fromtimestamp(datetime.now().timestamp()).strftime('%Y-%m-%d')
FILENAME = "MV_{}.pdf".format(DATE_STR)
FULLNAME = DATAPATH + FILENAME
HTML_URL = "https://www.lagus.mv-regierung.de/Gesundheit/InfektionsschutzPraevention/Daten-Corona-Pandemie"
SERVER   = "https://www.lagus.mv-regierung.de"

pdf_filename_pattern = re.compile(r"[a-zA-Z0-9_\-äöüÄÖÜ]*.pdf")

PDF_RE1  = re.compile(r"<a title=\"Download: MV-Lagebericht(.*?)>")
PDF_RE2  = re.compile(r"<a title=\"Download: Wöchentlicher Bericht über Zahl der Abstriche(.*?)>")
PDF_RE3  = re.compile(r"<a title=\"Download: Wöchentlicher Bericht zu Untersuchungsergebnissen in Kinderarzt(.*?)>")
PDF_RE4  = re.compile(r"<a title=\"Download: Lagebericht über COVID-19-Infektionen bei Gästen(.*?)>")

PDF_LINK = re.compile(r"href=\"(.*?)\"")

PDF_RES   = [ PDF_RE1, PDF_RE2, PDF_RE3, PDF_RE4 ]
PDF_NAMES = [ FULLNAME, DATAPATH + "MV_Abstriche_{}.pdf".format(DATE_STR), DATAPATH + "MV_Kinder_{}.pdf".format(DATE_STR), DATAPATH + "MV_Gäste_{}.pdf".format(DATE_STR) ]

if os.path.isfile(FULLNAME):

    if VERBOSE:
        print("The file '{}' exists already.".format(FILENAME))
        
    sys.exit(0)
    
else:
    
    if VERBOSE:
        print("The file '{}' does not exist.".format(FILENAME))
        
    pdf_files = []
    for r, d, f in os.walk(DATAPATH):
        for filename in f:
            if pdf_filename_pattern.match(filename):
                pdf_file = DATAPATH + filename
                sha256sum = hashlib.sha256(open(pdf_file,'rb').read()).hexdigest()
                pdf_files.append([filename, sha256sum])
                        
    headers = { 'Pragma': 'no-cache', 'Cache-Control': 'no-cache', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'de,en-US;q=0.7,en;q=0.3' }
    
    r = requests.get(HTML_URL, headers=headers, allow_redirects=True, timeout=5.0)
    if r.status_code != 200:
        print("Download failed!")
        sys.exit(1)
        
    i = -1
        
    for PDF_RE in PDF_RES:
        
        i += 1
        
        pre = PDF_RE.findall( r.text.replace("\n", "") )
        if len(pre) != 1:
            print("Download failed (link not found)!")
            continue
            
        pdf1 = PDF_LINK.findall(pre[0])
        if len(pdf1) != 1:
            print("Download failed (link not found)!")
            continue
            
        pdf1_url = SERVER + requests.utils.quote(pdf1[0])
        
        p = requests.get(pdf1_url, headers=headers, allow_redirects=True, timeout=5.0)
        if p.status_code != 200:
            print("PDF Download failed!")
            continue
        
        if not was_file_downloaded(pdf_files, p.content):            
            with open(PDF_NAMES[i], 'wb') as df:
                df.write(p.content)
                df.close()        
