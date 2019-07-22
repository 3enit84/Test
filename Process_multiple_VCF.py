
import os, glob, string

FileLst = FileNameLst = []
for filename in glob.glob1(VCF, "*.vcf"):
        FileLst = FileLst + [open(filename, "r")]#open all vcf files 
        FileNameLst = FileNameLst + [filename]#make a list of file names
print(FileNameLst)
for file_name in FileNameLst:#file_name is an xlsx file
        with open(file_name[:-4]+'tsv', 'w') as myCsvfile:
                # define a writer
                wr = csv.writer(myCsvfile, delimiter="\t")

                # open the xlsx file 
                myfile = xlrd.open_workbook(file_name)
                # get a sheet
                mysheet = myfile.sheet_by_index(0)

                # write the rows
                for rownum in range(mysheet.nrows):
                        wr.writerow(mysheet.row_values(rownum))
line = file.readline()

while line != "":
      rec = string.split(line,"\t")
      
      if rec[0][1] == "#":
            line = file.readline()
            continue
      else:          
            if rec[0][0] == "#": # Title line
                  newfile.write("SNP ID") #write SNP ID instead of just ID, which will convert output to SYLK format
                  for i in range(9,len(rec),2):
                        Smpl_ID = string.split(rec[i],".")
                        newfile.write("\t"+ Smpl_ID[0])
                  newfile.write("\n")
            else:
                  newfile.write(rec[2]) #write SNP ID
                  REF = rec[3]
                  ALT = rec[4]
                  for i in range(9,len(rec),2):
                        if len(rec[i]) > 5:
                              GT_a = rec[i][1]
                              GT_b = rec[i][3]   
                        elif len(rec[i+1]) > 5:                              
                              GT_a = rec[i+1][1]
                              GT_b = rec[i+1][3]           
                        else:
                              newfile.write("\tN/N") # No call
                              if i+1 == len(rec):
                                   newfile.write("\n")  
                              continue
                              
                        if int(GT_a) == 0:
                              GT_a = REF
                        else: GT_a = ALT

                        if int(GT_b) == 0:
                              GT_b = REF
                        else: GT_b = ALT
                        newfile.write("\t"+ GT_a +"/"+ GT_b)                   
                  newfile.write("\n")
      line = file.readline()

newfile.close()
file.close()
print "END"
