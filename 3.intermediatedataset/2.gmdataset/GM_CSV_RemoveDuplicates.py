# Remove duplicates

infile = open ("GM_Clean2_CorrectGeographyTerm.csv","r",encoding = "latin-1")

outfile = open ("GM_Clean3_CorrectGeographyTerm_withoutDuplicate.csv","w",encoding = "latin-1")

listlines = []

for line in infile:
    if line in listlines:
        continue
    else:
        outfile.write(line)
        listlines.append(line)
outfile.close()
infile.close()


