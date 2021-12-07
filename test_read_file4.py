import os
import datetime
file_stat = os.stat(os.path.join('documents','ZAPI_AGL_DD.csv'))
print(file_stat)
#print("Access Time is : "+str(file_stat.st_atime))
#print("Crated Time is : "+str(file_stat.st_ctime))
print(str(datetime.datetime.fromtimestamp(file_stat.st_atime))[0:19])
print(file_stat.st_size)