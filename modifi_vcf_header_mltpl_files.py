import os, glob

for filename in glob.glob1('COPD_fltrd/', "*COPD_filtered.vcf"):
        head = open('header.vcf', 'r')
        newhead = open(filename[:-18]+'_header.vcf', 'w')
        for h in head:
            if h[0:6] == '#CHROM':
                rec = str.split(h,'\t')
                for i in range(len(rec)-1):
                    newhead.write(rec[i] + '\t')#rewrite all head lines but last one
                newhead.write(filename[:-16] + '\n')#replace sample title with the 
            else: newhead.write(h)
        newhead.close()
        head.close()
