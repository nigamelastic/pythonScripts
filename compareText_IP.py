#this will check if data in compare1 exists in compare2

compare1='<input1.txt>'
compare2='<input2.txt>'

#output file
outputDiff='output\\outputDifference.csv'



file1Compare1 = open(compare1, 'r')
compare1Lines = file1Compare1.readlines()
compare1Lines = sorted(compare1Lines)

file2Compare2 = open(compare2, 'r')
compare2Lines = file2Compare2.readlines()
compare2Lines = sorted(compare2Lines)

outputDiffFile= open(outputDiff, 'a')


outputDiffFile.write('Matches from both the files are below:\n')

for line in compare2Lines:
    if line in compare1Lines:
        compare1Lines.remove(line)
        compare2Lines.remove(line)
        outputDiffFile.write(line+"\n")
        


outputDiffFile.write('Below are non duplicate entries from'+compare1 +'\n')
for value1 in compare1Lines:
    outputDiffFile.write(value1+"\n")

outputDiffFile.write('Below are non duplicate entries from'+compare2 +'\n')
for value2 in compare2Lines:
    outputDiffFile.write(value2+"\n")    
       
        
outputDiffFile.write('Below are non duplicate entries from'+compare2 +'\n')
outputDiffFile.close()
