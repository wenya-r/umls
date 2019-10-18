import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import collections


quiry_df = pd.read_excel("SiteSearch2019-01-uniquesForStep2.xlsx")
n_freq = 200
n_bucket = 3
pair = []
whole_list = []
bucket = [[],[], []]#[[]]*n_bucket
print("bucket = ", bucket)

for i_comp1 in range(500):
    comp1 = quiry_df['adjustedQueryTerm'][i_comp1]
    for i_comp2 in range(i_comp1+1, 500):
        comp2 = quiry_df['adjustedQueryTerm'][i_comp2]
        score = fuzz.ratio(comp1, comp2)
        if (score > 75):
            whole_list.extend((i_comp1, i_comp2))
            pair.append((i_comp1,i_comp2))
print("whole pair = ", pair)
whole_counter =  collections.Counter(whole_list)
whole_key = whole_counter.most_common(n_freq)
print(whole_key)
i_end = 0
i_cur = 0
i = 0
range_check = 0
for key, value in (whole_key):
#    print("key = ", key, "value = ", value)
    key_in_pre = False
# check whether key in previous bucket
    for j_check in range(max(range_check, i_end)):
        print("j_check = ", j_check)
        print("key = ", key)
        print("bucket[j_check] = ", bucket[j_check])
        print("key in buc ", key in bucket[j_check])
        if key in bucket[j_check]:
            key_in_pre = key in bucket[j_check]
            i_cur = j_check

        else:
            pass
    print( "What is i ", i)
    if (i_end == 0 and (bucket[0] == [])):
        i = 0
        range_check = 1
    elif ((key_in_pre)):
        i = i_cur
    elif (key_in_pre and i_end != 0):
        i = i_cur
    elif ((~key_in_pre) and (i_end < n_bucket)) :
        i_end = i_end + 1
        i = i_end
# end check whether key in previous bucket        

    print("i = " , i)   
    pair_copy = pair.copy()
    if (i < n_bucket):
      for i_pair in pair_copy:
        print("i_pair = ", i_pair)
        if(key == i_pair[0]):
            bucket[i].extend(i_pair)
            index = pair.index((key, i_pair[1]))
            print("index = ", index)
            pair.pop(index)            
        elif(key == i_pair[1]):          
            bucket[i].extend(i_pair)
        else:
            pass

        print( "bucket = ", bucket)    


for ii in range(n_bucket):
    print("bucket ", ii, " = ", [quiry_df['adjustedQueryTerm'][i_name] for i_name in set(bucket[ii])])
    print("\n")

#print("pair: " , pair)
#pair.pop(pair.index((15,27)))




#print(pair.index((15,27)))
