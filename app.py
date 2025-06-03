import random


# list of the house and 
pairs = []

house_list = ["James", "Mike M", "Eric", "Ben", "Roberto", "Mike F", "Chris", "Justin", "Cody", "Noah", "Joel", "Anthony"]


def create_random_pair(li):
    tmp_list = []
    
    name1 = random.choice(li)
    tmp_list.append(name1)
    name2 = random.choice(li)
    tmp_list.append(name2)

    while name1 == name2:
        name2 = random.choice(li)
        tmp_list[1] = name2
    
    print(tmp_list)
    return tmp_list    

# does_exist = False 

# counter = 0
# while does_exist == False:
#     counter =+ 1
#     pair_list = [create_random_pair(), create_random_pair()]
#     if pair_list[0] != pair_list[1]:
#         pairs.append(pair_list)
    
#     does_exist = True

create_random_pair(house_list)