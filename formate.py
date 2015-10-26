__author__ = 'joezhou'
import re

back_count_line_number = 21
try:
    with open('data3.txt') as f:
        lines = f.readlines()
        total_line= len(lines)
        if total_line - back_count_line_number > 0:
            line_items = lines[total_line - back_count_line_number].split()
            build_number = line_items [4]
            start_date = line_items [5]
except IOError:
    print ('No such file exist')
    exit
data_point = []
for line in lines:
    if re.search('(([0-9]+)_([0-9]+)_([0-9]+)_([0-9]+))',line):
        new_line = re.sub(', ',',',line)
        items = new_line.split()
        contents = items[1].split(',')
        for each_contents in contents:
            data_point.append(each_contents)

f.close()

print(data_point)
print('build number', build_number)
print('start time', start_date)
with open("build_number_date.txt",'w') as myfile:
    write_content= 'build_number:'+build_number+'\n'+'start_date:'+ start_date
    myfile.write(write_content)
myfile.close()




