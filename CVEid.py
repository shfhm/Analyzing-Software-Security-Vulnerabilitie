__author__ = 'Sahar'


import numpy as np
import pandas as pd
import csv
import re
data = pd.read_csv("myData3.csv")
K=data['cve.CVE_data_meta.ID'].values
count=0
key = 'CVE-2018-'
CVEid = []
for key in K:
    idNumber =0
    if len(key)>0:
        response = re.search(r'^(CVE-2018-)?(\d+)',key)
        idNumber = int(response.group(2))
    CVEid.append(idNumber)
CVEid

