import os, glob
from shutil import copyfile
copyfile('vcf_matrix.tsv', 'vcf_matrix_processed.tsv')

FileLst = FileNameLst = []
for filename in glob.glob("VCF/*.vcf"):
        FileLst = FileLst + [open(filename, "r")]#open all vcf files

for file in FileLst:
    pat_id = str.split(str(file),' ')[1][10:-7]#patient ID extracted from the file name
    #print(pat_id)
    pat_som_lst = [] #list of somatic mutetions for one patient
    line = file.readline()
    while line != "":
        if '#' in line:#skip header rows
            line = file.readline()
            continue
        else:
            rec = str.split(line,'\t')
            pat_som_lst += [rec[0]+'_'+rec[1]]
            line = file.readline()
            line = line.strip('\n')#some vcf files had lines with '\n' only at the end
    newfile = open('vcf_matrix_processed.tsv','r')
    tempfile = open('temp.tsv','w')
    newline = newfile.readline()#read the title line
    newline = newline.rstrip('\n')+'\t'+pat_id+'\n'
    tempfile.write(newline)
    newline = newfile.readline()
    while newline != "":           
        newrec = str.split(newline,'\t')
        if str.strip(newrec[0],'\n') in pat_som_lst:#the given mutation is in a given patient
            newline = newline.rstrip('\n')+'\t1\n'
        else: newline = newline.rstrip('\n')+'\t0\n'
        tempfile.write(newline)
        newline = newfile.readline()
    newfile.close()
    tempfile.close()
    copyfile('temp.tsv', 'vcf_matrix_processed.tsv')        
