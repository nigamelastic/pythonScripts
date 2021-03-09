import ipaddress
from subprocess import PIPE, Popen


inputFileWithIpSubnets = "<input filename with absolute path>"
outputCSVFileAbsolutePath = "<out csv filename with absolute path>"
file1 = open(inputFileWithIpSubnets, 'r')
Lines = file1.readlines()
file_object = open(outputCSVFileAbsolutePath, 'a')

for line in Lines:
    print(line)

    for ip in ipaddress.ip_network(line.strip()):

        ip = str(ip).strip()
   
        p = Popen('nslookup '+ip, shell=True, stdout=PIPE, stderr=PIPE)
        stdout, stderr = p.communicate()    
        
        output=str(stdout)
        error=str(stderr)
        if 'b\'\'' not in error:
            print(error)
            file_object.write(ip+';No Domain found;'+error.strip()+'\n')
        else:
            servername=output.split('Name:')[1].split('\\r\\n')[0]
            print(servername)
            file_object.write(ip+';'+servername.strip()+';'+output.strip()+'\n')
       
        

file_object.close()
