import os, glob

FileLst = FileNameLst = []
for filename in glob.glob("VCF/*.vcf"):
        FileLst = FileLst + [open(filename, "r")]#open all vcf files 
som_lst = [] #list of somatic mutetions
for file in FileLst:
    line = file.readline()
    while line != "":
        if '#' in line:#skip header rows
            line = file.readline()
            continue
        else:          
            rec = str.split(line,'\t')
            if rec[0]+'_'+rec[1] not in som_lst:
                som_lst += [rec[0]+'_'+rec[1]]                
        line = file.readline()
        line = line.strip('\n')#some vcf files had lines with '\n' only at the end
    file.close()
som_lst.sort()
newfile = open('vcf_matrix.tsv','w')
newfile.write('Position\n')#the title line
for som in som_lst:
    newfile.write(som + '\n')
