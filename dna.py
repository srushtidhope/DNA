#!/usr/bin/env python

# Code to get list of dna strands as input, filter through it to retain strands that meet conditions, and find common overlapping string sequence where last 3 characters of one strand are the same as first 3 characters of next strand

def filter_strands(strands):
    # Filter through dna strands to remove the ones that don't meet the conditions
    
    filtered_strands = []
    
    for strand in strands:
        if len(strand)==0:
            pass
        elif len(strand)>10:
            pass
        elif len(set(strand))>4:
            pass
        elif not set(strand).issubset(('A','T','G','C')):
            pass
        else:
            filtered_strands.append(strand)
    
    if len(filtered_strands)<3:
        return []
    else:
        return filtered_strands

def check_overlap(filtered_strands):
    # Find overlapping string from the filtered dna strands
    
    curr_strand = filtered_strands.pop(0)
    overlapping_string = curr_strand
    flag = 1
    
    while len(filtered_strands)>0:
        
        if flag==0:
            return ''
        else:
            flag = 0
        
        for strand in filtered_strands:
            if curr_strand[-3:]==strand[:3]:
                overlapping_string += strand[3:]
                curr_strand = strand
                filtered_strands.remove(strand)
                flag = 1
                break
    
    return overlapping_string

def analyze_dna(strands):
    # Filter through strand list and find overlapping string from it
    
    filtered_strands = filter_strands(strands)
    if filtered_strands == []:
        print("Invalid strands.. exiting.")
        return
    else:
        print("Filtered strands.. new length is ", len(filtered_strands))
    
    overlapping_string = check_overlap(filtered_strands)
    if overlapping_string == '':
        print("\n Overlapping string not found \n")
    else:
        print("\n Overlapping string is ", overlapping_string)

if __name__ == "__main__":
    
    strands = input("Enter dna strand list: ")
    analyze_dna(strands)
