# linux-utils: Linux system administration tools for Python.
#
# Author: Mahdi Khosravi <khosravi.mahdi73@gmail.com>

import os
import yaml
import subprocess
import datetime
import sys


u = ""
option = ""
FilePath = '/etc/fstab'
modifiedTime = os.path.getmtime(FilePath)

# Backup current fstab file.

timeStamp = datetime.datetime.fromtimestamp(modifiedTime).strftime("%b-%d-%y-%H:%M:%S")
try:
    os.rename(FilePath, FilePath + "_" + timeStamp)
except (OSError, PermissionError):
    print('please run script with sudo')

# Clean fstab file and ready to parse yaml file.

fsfile = open(FilePath, 'w')
fsfile.write('# <file system> <mount point>   <type>  <options>       <dump>  <pass>' + '\n')
fsfile.close()

# Open and process yaml file.

with open(sys.argv[1], "r") as file:
    try:
        output = yaml.safe_load(file)
        entries = output['fstab']
        for e in entries:
            for x in entries[e]:
                # To fetch list items options.
                if type(entries[e][x]) == list:
                    for z in entries[e][x]:
                        option = option + "," + z
                    break
                # To set reservation by cmd on disk because fstab doesn't support this option.
                if 'root-reserve' in x:
                    cmd = subprocess.run(["tune2fs", "-m10", f'{e}'], stdout=subprocess.DEVNULL)
                    return_code = cmd.returncode
                    if return_code == 0:
                        print(f'root-reserve on partition {e} has been modify it successfully')
                    else:
                        print(f'there is some problems to set root-reserve on partition {e},take look at syslog')
                    break
                # To place the exporter address next to the file-system address.
                if 'export' in x:
                    u = u + ":" + str(entries[e][x])
                else:
                    u = u + " " + str(entries[e][x])

            if ":" in u:
                final = e + u
            else:
                final = e + " " + u
            if (":" in final) and (option != ""):
                final = final + option.replace(",", " ", 1) + " 0 0"
            else:
                final = final + " defaults 0 0"
            # write to fstab file
            final_object = open(FilePath, 'a')
            final_object.write(final + "\n")
            final_object.close()
            u = ""
    except yaml.YAMLError as exc:
        print(exc)


# if you want to mount fstab after process finished please uncomment next line
# mountcmd = subprocess.run(["mount", "-a"])

