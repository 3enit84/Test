file = open('Significant_ID_Symbl.tsv', 'r')
newfile = open('Ancor_Symbl_IDs.tsv', 'w')
smbl_lst = []
probe_lst = []
line = file.readline()#title
line = file.readline()
sym = str.strip(str.split(line,'\t')[1])
while line != '':
    id_lst = []
    while sym == str.strip(str.split(line,'\t')[1]):
        id_lst += [str.split(line,'\t')[0]]
        line = file.readline()
        if line == '':
            break
    #print(sym,id_lst)
    if len(id_lst) == 1:
        newfile.write(sym+'\t'+id_lst[0]+'\n')
        probe_lst += [id_lst[0]]
    else:
        newfile.write(sym+'\t'+id_lst[0])
        probe_lst += [id_lst[0]]
        for i in range(1,len(id_lst)):
            newfile.write(','+ id_lst[i])
            probe_lst += [id_lst[0]]
        newfile.write('\n') 
    if line == "":
        break
    sym = str.strip(str.split(line,'\t')[1])#assign new gene symbol
file.close()
newfile.close()
print(len(probe_lst))
