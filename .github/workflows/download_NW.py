#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests, os, sys

VERBOSE  = True
DATAPATH = os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + ".." + os.sep + "data_NW" + os.sep

districts = [
        5, 
        5111, 5112, 5113, 5114, 5116,
        5117, 5119, 5120, 5122, 5124,
        5154, 5158, 5162, 5166, 5170,
        5314, 5315, 5316, 5334, 5358,
        5362, 5366, 5370, 5374, 5378,
        5382, 5512, 5513, 5515, 5554,
        5558, 5562, 5566, 5570, 5711,
        5754, 5758, 5762, 5766, 5770,
        5774, 5911, 5913, 5914, 5915,
        5916, 5954, 5958, 5962, 5966,
        5970, 5974, 5978 
    ]

for district in districts:
    
    CSV_URL  = "https://www.lzg.nrw.de/covid19/daten/covid19_{}.csv".format(district)
    FILENAME = "NW_covid19_{}.csv".format(district)
    FULLNAME = DATAPATH + FILENAME
        
    headers = { 'Pragma': 'no-cache', 'Cache-Control': 'no-cache' }
    
    r = requests.get(CSV_URL, headers=headers, allow_redirects=True, timeout=5.0)
    if r.status_code != 200:
        print("Download failed!")
        sys.exit(1)
        
    with open(FULLNAME, 'wb') as df:
        df.write(r.content)
        df.close()        
