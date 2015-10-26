import numpy as np
from scipy.stats import ttest_ind

step_len = 1
sample_len = 10
line = []
total_line_number = 0
for x2 in reversed(list(open("spy.txt"))):
    if x2 != 'null':
        x1 = x2.split('\t')
        #print(x1)
        line.append(float(x1[4]))
        total_line_number += 1
x = np.array(line)
#print(x)
y_total = x.astype(float)
y1=y_total[-sample_len:]
start_point = 0
drop_counter = 0
sum =0
drop_point = []
for start_point in range(0,len(y_total-sample_len-1),sample_len):
    y=y_total[start_point:start_point+sample_len]
    if len(y) == sample_len:
        #print ("y",y)
        #print ("y1",y1)
        t, p = ttest_ind(y, y1, equal_var=False)
        #print ("ttest_ind: t = %f  p = %f", t, p)
        #print(y)
        if p < 0.011 :
            drop_counter += 1
            print ("turn point happened",y_total[start_point+sample_len])
            drop_point.append(start_point+sample_len+1)
    y1 = y
if drop_counter > 0:
    print( "there are turnning point", drop_counter,"times", drop_point )
with open("spy.txt") as myfile:
    lines = myfile.readlines()
for drop_line in drop_point:
    print(lines[total_line_number-int(drop_line)])


myfile.close()
__author__ = 'joezhou'
