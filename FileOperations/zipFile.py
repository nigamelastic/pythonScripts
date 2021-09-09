import os
import zipfile
def unzipAndMove(folderLocation):
    folder = os.listdir(folderLocation)
    csvFolder=folderLocation+r'\\csvFiles'
    os.mkdir(csvFolder)

    for zipFileValue in folder:
        if zipFileValue.endswith(".zip"):
            zipdata = zipfile.ZipFile(folderLocation+r'\\'+zipFileValue)
            zipinfos = zipdata.infolist()
            # print(zipinfos)
            for zipinfo in zipinfos:
                zipinfo.filename=zipFileValue+r'_'+zipinfo.filename
                print(zipinfo.filename)
                zipdata.extract(zipinfo,csvFolder)
    for fileValue in folder:
        if fileValue.endswith(".csv"):
            print(fileValue)
            print(folderLocation+fileValue)
            os.rename(folderLocation+r'\\'+fileValue,csvFolder+r'\\'+fileValue)
