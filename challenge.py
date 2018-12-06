
import string, sys
from subprocess import call

filename = sys.argv[1]

file = open(filename, 'r')
#file = open("/media/sf_KFU/JH/Challenge_data.vcf",'r')      
bedfile = open("/media/sf_KFU/JH/Challenge_data.bed",'w')

SevLst = ['complex','del','ins','mnp','snp']#severity list
IdLst = VcfLst = []#list of SNV IDs and list of vcf data

line = file.readline()

while line != "":
      rec = str.split(line,"\t")
      #print(rec[0][1])
      if line[0] == "#": #skip header entries and the title line
            line = file.readline()
            continue
      else:            
            EndPoints = str.split(rec[7],";")#allele call data
            CovData = str.split(rec[9],":")#coverage data
            DP = CovData[2]#depth
            Alt = CovData[6]#variant coverage
            AltNuc = rec[4]#Nuceleotade sequence of ALT
            for Type in EndPoints:
                  T = str.split(Type,"=")
                  if T[0] == "TYPE":
                        AltLst = str.split(T[1],",")#list of detected alterations
                        AltCov = str.split(Alt,",")#list of coverages for each alteration
                        if len(AltLst) > 1:#more than one call for SNV
                              for Snv in SevLst:
                                    if Snv in AltLst:
                                          Alt = AltCov[AltLst.index(Snv)]#the correcponding to Alt coverage
                                          AltNuc = rec[4][AltLst.index(Snv)]#the correcponding to Alt nuc sequence
                                          break                           
                        else:
                              PerAlt = float(Alt)/float(DP)*100.0#Percentage Alt vs Ref
                              Snv = AltLst[0]#type of SNV
            IdLst = IdLst + [str(rec[0]) +"_"+ str(rec[1])]     
            VcfLst = VcfLst +[[Snv,DP, Alt, str(round(PerAlt))+"/"+str(round(100-PerAlt))]]
            
            
            SnvEnd = int(rec[1]) + len(rec[3]) - 1#end of SNV
            bedfile.write(rec[0] +"\t"+ rec[1] +"\t"+ str(SnvEnd) +"\t"+ rec[3] +"\t"+ AltNuc +"\n")                   
            
      line = file.readline()

bedfile.close()
file.close()

command = ("perl table_annovar.pl /media/sf_KFU/JH/Challenge_data.bed humandb/ -buildver hg19 -out Challenge_data_anno -remove -protocol refGene,cytoBand,exac03,avsnp147,dbnsfp30a -operation gx,r,f,f,f -nastring . -csvout -polish -xref example/gene_xref.txt")
print(command)
call(command, shell = True)

file = open("/media/sf_KFU/PRGRMS/annovar/Challenge_data_anno.hg19_multianno.txt",'r')#VCF_tst.txt
newfile = open("/media/sf_KFU/PRGRMS/annovar/Challenge_data_prcssd.txt",'w')

line = file.readline()#title
rec = str.split(line,"\t")
for i in range(5):
      newfile.write(rec[i] + "\t")
newfile.write("Type of alteration\tExonic function\tDepth of coverage\tNumber of variant reads\t\
% of variant reads\tExAC\tExAC African\tExAC American\n")
line = file.readline()#first SNV data
while line != "":
      rec = str.split(line,"\t")
      for i in range(5):
            newfile.write(rec[i] + "\t")
      ID = str(rec[0]) +"_"+ str(rec[1])
      #print(ID)
      if ID in IdLst:
            VcfLst[IdLst.index(ID)].insert(1,rec[8])#Exonic function
            VcfLst[IdLst.index(ID)].append(rec[12])#Exac all
            VcfLst[IdLst.index(ID)].append(rec[13])#Exac african
            VcfLst[IdLst.index(ID)].append(rec[14])#Exac american
      for i in range(8):
            if i == 7:
                  newfile.write(str(VcfLst[IdLst.index(ID)][i]) + "\n")
            else: newfile.write(str(VcfLst[IdLst.index(ID)][i]) + "\t")
      line = file.readline()

file.close()
newfile.close()
print("\n\n\nAnnotated output file is written to Challenge_data_prcssd.txt")

