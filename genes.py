# File: genes.py
# Author: Pete Sripitak
# Finds all hypothetical genes (codons in the same reading frame).
# From a file with sample genes

#!/usr/local/bin/python3.2

import sys 

f = open(sys.argv[1])
lines = f.readlines()
#print(lines)
print()

for line in lines:
    line = line.replace('\n','')
    line = line.replace('\t','')
    line = line.rstrip()
    line = line.split()
    #print(line)
    seq_id = line[0]
    #print(seq_id)
    line[1] = line[1].upper()
    char_list = list(line[1])
    char_list_max = len(char_list) - 3
    #print(char_list)
    #print(len(char_list))
    
    #if len(char_list) < 33 or len(char_list) > 99:
        #continue
    
    found_start = False
    i = 0
    start_codon = char_list[i] + char_list[i+1] + char_list[i+2]
    
    if start_codon == 'ATG' or start_codon == 'GTG':
        start_loc = i
        found_start = True
    
    while not found_start:
        i += 1
        start_codon = char_list[i] + char_list[i+1] + char_list[i+2]
        if start_codon == 'ATG' or start_codon == 'GTG':
            start_loc = i
            found_start = True
        elif i == char_list_max:
            break
    
    if i == char_list_max:
        continue
    
    #if found_start:
        #print()
        #print(seq_id, start_loc, start_codon)
        #print()
        
    found_start_2 = found_stop = found_stop_2 = False
    i += 3
    count = count_2 = 3
    stop_codon = char_list[i] + char_list[i+1] + char_list[i+2]
    
    if stop_codon == 'ATG' or stop_codon == 'GTG':
        start_codon_2 = stop_codon
        start_loc_2 = i
        found_start_2 = True
    elif stop_codon == 'TAG' and count >= 30 and count <= 96:
        stop_loc = count + 3
        found_stop = True
    elif stop_codon == 'TAG' and count < 30:
        continue
    elif stop_codon == 'TAG' and count > 96:
        continue
    
    while not found_stop:
        i += 1
        count += 1
        stop_codon = char_list[i] + char_list[i+1] + char_list[i+2]
        if stop_codon == 'ATG' or stop_codon == 'GTG':
            start_codon_2 = stop_codon
            count_2 = count
            #print(count_2)
            #print()
            start_loc_2 = i
            found_start_2 = True
        elif stop_codon == 'TAG' and count >= 30 and count <= 96:
            stop_loc = count + 3
            found_stop = True
        elif stop_codon == 'TAG' and count < 30:
            break
        elif stop_codon == 'TAG' and count > 96:
            break
        elif i == char_list_max:
            break
    
    if i == char_list_max:
        continue
    
    found_stop_shared = False
    
    if found_start_2:
        #print(count_2)
        #print(stop_loc)
        #print(stop_loc - count_2)
        if (stop_loc - count_2) >= 30 and (stop_loc - count_2) <= 96:
            found_stop_shared = True
            stop_codon_2 = stop_codon
            stop_loc_2 = stop_loc - count_2
            found_stop_2 = True
    
    if found_start_2 and not found_stop_shared:
        i += 3
        count_2 = stop_loc - count_2
        while not found_stop_2:
            i += 1
            count_2 += 1
            stop_codon_2 = char_list[i] + char_list[i+1] + char_list[i+2]
            if stop_codon_2 == 'TAG' and count_2 >= 30 and count_2 <= 96:
                stop_loc_2 = count_2 + 3
                found_stop_2 = True
            elif stop_codon_2 == 'TAG' and count_2 < 30:
                break
            elif stop_codon_2 == 'TAG' and count_2 > 96:
                break
            elif i == char_list_max:
                break
    
    if found_stop:
        print(seq_id, start_loc, stop_loc, start_codon, stop_codon)
    
    if found_stop_2:
        print(seq_id, start_loc_2, stop_loc_2, start_codon_2, stop_codon_2)
    
print()
