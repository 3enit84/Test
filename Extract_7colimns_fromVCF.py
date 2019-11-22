import os, glob
from multiprocessing import Pool
from subprocess import call

FileNameLst = []
for filename in glob.glob('NWD*v1.vcf'):
    FileNameLst = FileNameLst + [filename]#make a list of file names
print(FileNameLst[0:4])
def process_file(infile):#function to run each file through tabix
    file = open(infile,'r')#read file in the list
    outfile = open('shrt_'+infile,'w')
    for line in file:
        if line[0] == "#":#skip header
            continue
        else:
            if str(1) in str.split(line,"\t")[9]:
                outfile.write(line)
                
if __name__ == "__main__":
    pool = Pool(8)#number of nodes to be used
    results = pool.map(process_file, FileNameLst)
