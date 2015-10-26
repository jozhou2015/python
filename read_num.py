__author__ = 'joezhou'

try:
    with open('data2.txt') as f:
        lines = f.readlines()
        print(lines)
        total_line= len(lines)
        if total_line -15 >0:
            print ('number',lines[total_line-15])
except IOError:
    print ('No such file exist')
    exit

