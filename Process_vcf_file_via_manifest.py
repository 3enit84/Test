file_name = 'data/manifest-2019-07-16T15-56-46.245144/by-filename/NWD111050.freeze5.v1.vcf.gz'
filter_file = 'cardio.bed'

from csv import reader
import io
filterfile = open(filter_file, 'r')
flt_lst = []#filter list
for rec in reader(filterfile, delimiter='\t'):
    flt_lst += [[rec[0],int(rec[1]), int(rec[2])]]
print('List is ready')
filterfile.close()

file = io.TextIOWrapper(gzip.open(file_name, 'r'))
newfile = open('NWD111050_filtered.vcf','w')
line = file.readline()
newfile.write(line)
while line != "":
    rec = str.split(line,'\t')
    for f in flt_lst:
        if f[0] == rec[0]:#the same chromosome
            if f[1]<=int(rec[1])<=f[2]:
                newfile.write(line)
    line = file.readline()
file.close()
newfile.close()  
