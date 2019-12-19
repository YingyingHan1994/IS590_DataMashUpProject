# Remove duplicated rows
infile = open ("saam_WebConGeography_raw.csv","r",encoding = "latin-1")

outfile = open ("saam_WebConGeography_CleanDataRemoveDuplicates.csv","w",encoding = "latin-1")

listlines = []

for line in infile:
    if line in listlines:
        continue
    else:
        outfile.write(line)
        listlines.append(line)
outfile.close()
infile.close()
