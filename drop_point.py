import numpy as np
from scipy.cluster.vq import kmeans, vq
import re
from scipy.stats import ttest_ind

step_len = 5
sample_len = 15
def get_data_formate():
    try:
        with open('drop_point_data.txt') as f:
            lines = f.readlines()
    except IOError:
        print ('No such file exist')
        exit
    data_point = ''
    for line in lines:
        if re.search('(([0-9]+)_([0-9]+)_([0-9]+)_([0-9]+))',line):
            new_line = re.sub(', ',',',line)
            items = new_line.split()
            contents = items[1].split(',')
            for each_contents in contents:
                data_point += str(each_contents) + "\n"
    f.close()
    #print(data_point)
    with open("formate_data.txt",'w') as myfile:
        myfile.write(data_point)
    myfile.close()

def get_bottom_bond(y):
    rg=[]
    codebook, _ = kmeans(y, 3)  # three clusters
    cluster_indices, _ = vq(y, codebook)
    print (y)
    #print ('cluster 1\n')
    #print (y[cluster_indices==0])
    #for indic in cluster_indices:
    if len(y[cluster_indices==0]) > (sample_len / 5):
        first_bar = float(sum(y[cluster_indices==0])/ len(y[cluster_indices==0]))
        #print ("hl",first_bar)
        rg.append(first_bar)
    if len(y[cluster_indices==1]) > (sample_len / 5):
        second_bar = float(sum(y[cluster_indices==1])/ len(y[cluster_indices==1]))
        #print ("h2",second_bar)
        rg.append(second_bar)
    if len(y[cluster_indices==2]) > (sample_len / 5):
        third_bar = float(sum(y[cluster_indices==2])/ len(y[cluster_indices==2]))
        #print ("h3",third_bar)
        rg.append(third_bar)
    #print ('cluster 2\n')
    #print (y[cluster_indices==1])
    #print ('cluster 3\n')
    #print (y[cluster_indices==2])
    print ('rang',rg)
    top_limit = max(rg)
    bottom_limit = min(rg)
    print ("toper limit",top_limit)
    print ("toper bottom", bottom_limit)
    return bottom_limit

def find_max_drop_section():
    try:
        with open('formate_data.txt') as f:
            lines = f.read().splitlines()
            line =[]
            for x in lines:
                if x != 'null':
                    line.append(float(x))
    except IOError:
        print ('NP file No such file exist')
        exit
    x = np.array(line)
    y_total = x.astype(float)
    y1=y_total[-sample_len:]
    bottom_limit_left = get_bottom_bond(y1)
    print ('left_bond',bottom_limit_left)
    start_point = 0
    percentage_array=[]
    for start_point in range(0,len(y_total),step_len):
        y=y_total[start_point:start_point+sample_len]
        if len(y) > 13 :
            bottom_limit_right = get_bottom_bond(y)
            #print (bottom_limit_right)
            percentage_array.append(abs((bottom_limit_right-bottom_limit_left)*100/bottom_limit_left))
           # if abs((bottom_limit_right-bottom_limit_left)*100/bottom_limit_left) > 1 :
            #    print ("droped = ""{0:.3f}%".format(((bottom_limit_right-bottom_limit_left)*100/bottom_limit_left)))
            #else:
            #    print ("no drop = " "{0:.3f}%".format(((bottom_limit_right-bottom_limit_left)*100/bottom_limit_left)))

    #max_drop = max(percentage_array)
    print(percentage_array)
    max_position = 0
    max_drop = 0
    count = 0
    for percentage_item in percentage_array:
        if percentage_item > max_drop:
            max_drop = percentage_item
            max_position = count
            count += 1

    if max_drop > 1 :
        print ("droped = ""{0:.3f}%".format(max_drop), "position=", max_position)
    else:
        print ("no drop = " "{0:.3f}%".format(max_drop))
    t_test(max_position)


def t_test(max_position):
    t_sample_len = 3
    try:
        with open('formate_data.txt') as f:
            lines = f.read().splitlines()
            line =[]
            for x in lines:
                if x != 'null':
                    line.append(float(x))
    except IOError:
        print ('test file No such file exist')
        exit
    f.close()
    y_total = line
    start_section_point = step_len * max_position
    print('start',start_section_point)
    t_test_y = y_total[start_section_point:start_section_point+sample_len]
    print(t_test_y)
    y1=t_test_y[-t_sample_len:]
    #y1 = y_total[-t_sample_len:]
    drop_counter = 0
    for start_point in range(0,sample_len):
        y=t_test_y[start_point:start_point+t_sample_len]
        if len(y) == t_sample_len:
            #print ("y",y)
            #print ("y1",y1)
            t, p = ttest_ind(y, y1, equal_var=False)
            #print ("ttest_ind: t = %f  p = %f", t, p)
            if p < 0.01 :
                drop_counter += 1
                global_drop_position = start_point + 1+ start_section_point
                print ("drop happened at position",global_drop_position)
                break
        #y1 = y
    if drop_counter > 0:
        print( "there are drops", drop_counter,"times" )

    try:
        with open('drop_point_data.txt') as f:
            lines = f.readlines()
    except IOError:
        print ('No such file exist')
        exit
    line_count = 0
    for line in lines:
        if re.search('(([0-9]+)_([0-9]+)_([0-9]+)_([0-9]+))',line):
            line_count += 1
            if line_count == global_drop_position:
                new_line = re.sub(', ',',',line)
                items = new_line.split()
                build_number_at_drop = items[2].split(',')
                print(build_number_at_drop)
    f.close()
    #print(data_point)



def find_max_drop_point_t_test():
    pass

def find_drop_point_build_number():
    pass


if __name__ == "__main__":
    get_data_formate()
    find_max_drop_section()
    find_max_drop_point_t_test()
    find_drop_point_build_number()

