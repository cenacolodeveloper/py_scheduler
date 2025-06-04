# import random
from itertools import combinations
import pandas

EXCEL_FILE = "house_list.xlsx"

res = pandas.read_excel(EXCEL_FILE)


def arr_to_str(arr):
    return arr[0]

cleaned_excel_list = list(map(arr_to_str, res.values))


if len(cleaned_excel_list) % 2 != 0:
   raise Exception("House List must have even number of brothers")
    
def write_data_to_excel():
    data = {'col1': [1, 2], 'col2': [3, 4]}
    df = pandas.DataFrame(data)

    # Write to Excel file
    df.to_excel("output.xlsx")


def rSubset(arr):
    c = list(combinations(arr, 2))
    print(len(c))
    return list(combinations(arr, 2))


# write_data_to_excel()
print(rSubset(cleaned_excel_list))










# arr = ["James", "Mike M", "Eric", "Ben", "Roberto", "Mike F", "Chris", "Justin", "Cody", "Noah", "Joel", "Anthony"]
 
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