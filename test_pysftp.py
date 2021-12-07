import pysftp
from stat import S_ISDIR , S_ISREG
import os
import os.path

cnopts =pysftp.CnOpts()
cnopts.hostkeys = None
myHostname = "chbwapp001"
myUserName = "root"
myPassword = "Maxim123"
with pysftp.Connection(host=myHostname, username=myUserName, password=myPassword, cnopts=cnopts) as sftp:
    with sftp.cd("\\chbwapp001\wwwroot\VideoUp"): #put path of server
        sftp.put(os.path.join("log","lod_daily_alert_line_25.txt"))   
        
        '''
        directory_structure = sftp.listdir_attr()
        for attr in directory_structure:
            file_to_get = os.path.join("log",attr.filename)
            if attr.filename.startswith("REG") and attr.filename.endswith("26.TXT"):
                sftp.get(attr.filename,file_to_get) '''
