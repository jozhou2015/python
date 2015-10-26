__author__ = 'joezhou'

with open('select_file.txt','r') as infile:
    lines = infile.readlines()
di = dict{}
uniq_lines = set(lines)
for line in uniq_lines:
    g = line.split()


