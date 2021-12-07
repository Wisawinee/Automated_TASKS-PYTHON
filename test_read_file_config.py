import os
import xml.etree.ElementTree as ET

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
print(var_PathToPlaceLog,var_PathToDeleteFile,var_DaysToKeepFile)