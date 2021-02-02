
import os

csvFolderName = r'pathtocsv'
for file in os.listdir(csvFolderName):
    
    if '.csv' in file:
        with open(csvFolderName+'/'+file, 'r') as f:
           filedata = f.read()
           filedata = filedata.replace(',', ';')
           filedata = filedata.replace('.',',')
           
           f.close()
        with open(csvFolderName+'/'+file, 'w') as f:
            f.write(filedata)
            f.close()