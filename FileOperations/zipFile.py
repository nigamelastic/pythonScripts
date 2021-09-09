import os
import zipfile
def unzipAndMove(folderLocation):
    folder = os.listdir(folderLocation)
    csvFolder=folderLocation+r'\\csvFiles'
    #making a directory
    os.mkdir(csvFolder)

    for zipFileValue in folder:
        if zipFileValue.endswith(".zip"):
            zipdata = zipfile.ZipFile(folderLocation+r'\\'+zipFileValue)
            zipinfos = zipdata.infolist()
            # print(zipinfos)
            for zipinfo in zipinfos:
                #changing the Filename value in the archive
                zipinfo.filename=zipFileValue+r'_'+zipinfo.filename
                print(zipinfo.filename)
                #extracting the file with specific folder location
                zipdata.extract(zipinfo,csvFolder)
                
                
                
    for fileValue in folder:
        if fileValue.endswith(".csv"):
            
            print(folderLocation+fileValue)
            #moving the file
            os.rename(folderLocation+r'\\'+fileValue,csvFolder+r'\\'+fileValue)
