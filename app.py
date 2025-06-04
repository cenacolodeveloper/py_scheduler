# import random
from itertools import combinations
import pandas


res = pandas.read_excel("house_list.xlsx")
print(res.values)

def arr_to_str(arr):
    return arr[0]

cleaned_excel_list = list(map(arr_to_str, res.values))


if len(cleaned_excel_list) % 2 != 0:
   raise Exception("House List must have even number of brothers")
    



def rSubset(arr, r):
    c = list(combinations(arr, r))
    print(len(c))
    return list(combinations(arr, r))

arr = ["James", "Mike M", "Eric", "Ben", "Roberto", "Mike F", "Chris", "Justin", "Cody", "Noah", "Joel", "Anthony"]
r = 2

# print(rSubset(arr, r))





 
# pairs = []

# house_list = ["James", "Mike M", "Eric", "Ben", "Roberto", "Mike F", "Chris", "Justin", "Cody", "Noah", "Joel", "Anthony"]


# def create_random_pair(li):
#     tmp_list = []
    
#     name1 = random.choice(li)
#     tmp_list.append(name1)
#     name2 = random.choice(li)
#     tmp_list.append(name2)

#     while name1 == name2:
#         name2 = random.choice(li)
#         tmp_list[1] = name2
    
#     return tmp_list    

# def get_combinations(l):
#     house_list_length = len(l)
# def create_pairs():
#     p = create_random_pair(house_list)
#     pairs.append(p)
#     print(pairs)

# create_pairs()