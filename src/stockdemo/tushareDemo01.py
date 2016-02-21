# -*- coding: utf-8 -*-

import tushare as ts
import pandas as pd
import time


from sqlalchemy import create_engine
import tushare as ts

try:
    import json
except ImportError:
    import simplejson as json

##用tushare库找到当日涨停股票

with open("config.json",'rt') as jsonFile:
    val = jsonFile.read()
    config = json.loads(val);

allData = ts.get_today_all()
upDate = time.strftime("%Y-%m-%d",time.localtime())
upFileName = "UP"+upDate+".csv"

allDataFileName = "allData"+upDate+".csv"

outputAllDataFileDir = config['outputDir'] + "/" + allDataFileName

outputUpDataFileDir = config['outputDir'] + "/" + upFileName

upData = allData[allData.changepercent > 9.9]

upData.to_csv(outputUpDataFileDir,encoding='gbk')
allData.to_csv(outputAllDataFileDir,encoding='gbk')

outputAllDataFileDir = config['outputDir'] + "/" + allDataFileName

upData = pd.read_csv(outputUpDataFileDir,encoding='gbk',index_col =0,dtype={'code':str})

print(upData['code'])



