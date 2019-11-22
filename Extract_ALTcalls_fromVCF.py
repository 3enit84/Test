import os, glob
from multiprocessing import Pool
from subprocess import call
import gzip

FileNameLst = []
for filename in glob.glob('NWD*v1.vcf.gz'):
    FileNameLst = FileNameLst + [filename]#make a list of file names
print(FileNameLst[0:4])
def process_file(infile):#function to run each file through tabix
    command = ('bgzip -d '+infile)#decompress bgzip file
    call(command, shell = True)
    file = open(infile[0:-3],'r')#read file in the list
    outfile = open('shrt_'+infile[0:-3],'w')
    for line in file:
        if line[0] == "#":#skip header
            continue
        else:
            if str(1) in str.split(line,"\t")[9]:
                outfile.write(line)

if __name__ == "__main__":
    pool = Pool(2)#number of nodes to be used
    results = pool.map(process_file, FileNameLst)
