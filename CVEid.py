__author__ = 'Sahar'


import pandas as pd
import re
data = pd.read_csv("myData3.csv")
CVE_ID=data['cve.CVE_data_meta.ID'].values
count=0
key = 'CVE-2018-'
ID = []
for key in CVE_ID:
    idNumber =0
    if len(key)>0:
        response = re.search(r'^(CVE-2018-)?(\d+)',key)
        idNumber = int(response.group(2))
    ID.append(idNumber)
ID

