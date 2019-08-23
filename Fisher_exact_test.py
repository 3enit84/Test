import scipy.stats
import numpy as np
from numpy import *
from array import *

file = open('kf-cohort.processed_sift_ann.vcf', 'r')#kf-cohort.processed_sift_ann.vcf  AF_merged_ann.vcf
newfile = open('KF_deleterious_counted.tsv', 'w')
for line in file:
    if line[0] == '#':
        continue #skip headers
    if '_pred' in line:#select entries with predicted effects
        rec = str.split(line, '\t')
        calls = str.split(rec[7],';')
        call_cnt = 0
        for c in calls:
            if '_pred' in c:
                eff = str.split(c,'_pred=')#effects of SNP
                if eff[1][0] == 'D':
                    call_cnt += 1               
        if call_cnt > 2:#at least 3 programs called it deleterious
            allele_cnt = 0
            for i in range(9,len(rec)):#count all entries for alleles
                if int(rec[i][0]) == 1:
                    allele_cnt += 1
                if int(str.strip(rec[i][2])) == 1:
                    allele_cnt += 1
            obs_alt = allele_cnt #observed alternate alleles
            obs_tot = (len(rec)-9)*2 #total alleles
            if allele_cnt > 0.05*(len(rec)-9)*2:#5% out of all allele calls
                Fish = [1,1]
                for c in calls:
                    if 'ExAC_Adj_AC' in c:
                        ac = str.split(c,'ExAC_Adj_AC=')#ExAC allele count
                        exp_alt = int(ac[1]) #expected alternate alleles
                    if 'ExAC_Adj_AF' in c:
                        af = str.split(c,'ExAC_Adj_AF=')#ExAC allele frequency
                        exp_tot = round(exp_alt/float(af[1]))
                cntrl = np.array([exp_alt,exp_tot-exp_alt]) #control
                cond = np.array([obs_alt,obs_tot-obs_alt]) #condition
                Fish = scipy.stats.fisher_exact([cntrl,cond])
                if Fish[1] < 0.05:
                    print('Fisher_test = ',Fish[1])
                    print(rec[0],rec[1],rec[2],rec[3]+rec[4],allele_cnt, (len(rec)-9)*2-allele_cnt, float(allele_cnt/(len(rec)-9)*2))
                    newfile.write(rec[0]+'\t'+str(rec[1])+'\t'+rec[2]+'\t'+rec[3]+rec[4]+'\t'\
                                  +str(allele_cnt)+'\t'+str(float(allele_cnt/(len(rec)-9)*2))+'\n')          
newfile.close()
