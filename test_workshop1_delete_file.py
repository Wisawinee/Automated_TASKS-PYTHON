import os
import xml.etree.ElementTree as ET
import time
import datetime
from datetime import date

def remove_file(var_PathToDeleteFile,os,var_PathToPlaceLog,log_daily,current_time,var_DaysToKeepFile):
    for file in os.listdir(var_PathToDeleteFile):
        path_file = os.path.join(var_PathToDeleteFile,file)
        if os.path.isfile(path_file):
            creation_time = os.path.getctime(path_file)
            if(current_time - creation_time) // (24*3600) >= int(var_DaysToKeepFile):
                os.remove(path_file)
                log_transaction(var_PathToPlaceLog,log_daily,"a","Remove file"+file)
    log_transaction(var_PathToPlaceLog,log_daily,"a","Remove file from success")

def log_transaction(var_PathToPlaceLog,log_daily,mode_write_file,string_to_write_log):
     today = str(date.today())
     result_log_daily = open(os.path.join(var_PathToPlaceLog,log_daily),mode_write_file,encoding="tis-620",errors='ignore')
     result_log_daily.write(today+" "+get_local_time()+" : "+string_to_write_log+" \n")
     result_log_daily.close()

def get_local_time():
     local_time = str(time.ctime(time.time()))[11:20]
     return local_time

file_config = 'automated_task_file.config'
root = ET.parse(file_config).getroot()
var_PathToPlaceLog = ""
var_PathToDeleteFile = ""
var_DaysToKeepFile = ""
var_path_soure = os.getcwd()
for data in root:
    for detail in data:
        if(detail.get('key')=="PathToPlaceLog"):
            var_PathToPlaceLog = var_path_soure+detail.get('value')
        elif(detail.get('key')=="PathToDeleteFile"):
            var_PathToDeleteFile = detail.get('value')
        elif(detail.get('key')=="DaysToKeepFile"):
            var_DaysToKeepFile = detail.get('value')
current_time = time.time()
today = str(date.today())
today_date_current = int(today[8:10])

log_daily = "log_daily_alert_line_"+str(today_date_current)+".txt"
log_transaction(var_PathToPlaceLog,log_daily,"w+","Start Housekeeping File")
log_transaction(var_PathToPlaceLog,log_daily,"a","Destination Path for housekeeping is" +var_PathToDeleteFile)
remove_file(var_PathToDeleteFile,os,var_PathToPlaceLog,log_daily,current_time,var_DaysToKeepFile)