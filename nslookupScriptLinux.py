#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import ipaddress
from subprocess import PIPE, Popen

if len(sys.argv) != 3:
    print(len(sys.argv))
    for val in sys.argv:
        print(val)
    print('invalid number of argument!!')
    print("Usage: ./nslookupScriptLinux.py <input file containing ip addresses> <outputfile>")
    print("Example: ./nslookupScriptLinux.py ip.txt output.csv")
    sys.exit('Please use the syntax mentioned above and try again')



#Insert your input and output filenames:
inputFileName= sys.argv[1]
outputFileName=sys.argv[2]


file1 = open(inputFileName, 'r')
Lines = file1.readlines()
file_object = open(outputFileName, 'a')

for line in Lines:
    print(line)

    for ip in ipaddress.ip_network(line.strip()):

        ip = str(ip).strip()
   
        p = Popen('nslookup '+ip, shell=True, stdout=PIPE, stderr=PIPE)
        stdout, stderr = p.communicate()    
        
        output=str(stdout)
        
        print("_____________________________________")
        
        if 'can\'t find ' in output:
            print(output)
            file_object.write(ip+';No Domain found;'+output.strip()+'\n')
        else:
            servername=output.split('name =')[1].split('\\n')[0]
            print(servername)
            file_object.write(ip+';'+servername.strip()+';'+output.strip()+'\n')
       
        

file_object.close()
