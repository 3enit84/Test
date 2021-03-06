import os, glob
from multiprocessing import Pool
from subprocess import call

FileNameLst = []
for filename in glob.glob('*.vcf.gz'):
        FileNameLst = FileNameLst + [filename]#make a list of file names

def process_file(infile):#function to run each file through tabix
        #grep all lines where the 10th column contains at least one 1 (alternate allele)
        command = ("zcat "+infile+"|awk -F'\t' '$10~/1/'>"+infile[0:-3]+"_alt.tsv")
        call(command, shell = True)
        return print(command)

if __name__ == "__main__":
    pool = Pool(24)#number of nodes to be used
    results = pool.map(process_file, FileNameLst)
    print('processed '+str(len(results))+' files')
