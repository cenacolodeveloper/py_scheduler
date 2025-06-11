from itertools import combinations
import pandas
import random

EXCEL_FILE = "house_list.xlsx"
number_of_combos = 0

def arr_to_str(arr):
    return arr[0]

res = pandas.read_excel(EXCEL_FILE)
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
    global number_of_combos
    number_of_combos = len(c)
    return c

def getRandomTuple(hs_list):
    return random.choice(hs_list)
    


def fill_scheduling_session(hs_list, num_pairs):
    tmp_session = []
    while len(tmp_session) < num_pairs:
        r = getRandomTuple(hs_list)

        if len(tmp_session) == 0:
            tmp_session.append(r)
            continue

        bo = False
        for x in range(0, len(tmp_session)):
            a = tmp_session[x][0]
            b = tmp_session[x][1]

            if(r[0] == a or r[0] == b or r[1] == a or r[1] == b):
                bo = True
                break
            else:
                continue
        if bo == False:
            tmp_session.append(r)
  
        # for x in range(0, len(tmp_session)):
        #     if tmp_session[x]
        
        # if len(tmp_session) == 0:
        #     tmp_session.append(r)
      
    print(tmp_session)
    return tmp_session

# write_data_to_excel()
house_list_tuples = rSubset(cleaned_excel_list)
# print(house_list_tuples)

number_of_schedulingPairs_per_session = number_of_combos/(len(cleaned_excel_list) - 1)


fill_scheduling_session(house_list_tuples, number_of_schedulingPairs_per_session)




#       SAMPLE OUTPUT

#       [('James', 'Mike M'), ('James', 'Anthony'), ('James', 'Ben'), ('James', 'Roberto'), ('James', 'Eric '), 
#       ('James', 'Mike F'), ('James', 'Chris'), ('James', 'Joel'), ('James', 'Noah'), ('James', 'Cody'), 
#       ('James', 'Justin'), ('Mike M', 'Anthony'), ('Mike M', 'Ben'), ('Mike M', 'Roberto'), ('Mike M', 'Eric '),
#       ('Mike M', 'Mike F'), ('Mike M', 'Chris'), ('Mike M', 'Joel'), ('Mike M', 'Noah'), ('Mike M', 'Cody'),
#       ('Mike M', 'Justin'), ('Anthony', 'Ben'), ('Anthony', 'Roberto'), ('Anthony', 'Eric '), ('Anthony', 'Mike F'),
#       ('Anthony', 'Chris'), ('Anthony', 'Joel'), ('Anthony', 'Noah'), ('Anthony', 'Cody'), ('Anthony', 'Justin'),
#       ('Ben', 'Roberto'), ('Ben', 'Eric '), ('Ben', 'Mike F'), ('Ben', 'Chris'), ('Ben', 'Joel'), ('Ben', 'Noah'),
#       ('Ben', 'Cody'), ('Ben', 'Justin'), ('Roberto', 'Eric '), ('Roberto', 'Mike F'), ('Roberto', 'Chris'),
#       ('Roberto', 'Joel'), ('Roberto', 'Noah'), ('Roberto', 'Cody'), ('Roberto', 'Justin'), ('Eric ', 'Mike F'),
#       ('Eric ', 'Chris'), ('Eric ', 'Joel'), ('Eric ', 'Noah'), ('Eric ', 'Cody'), ('Eric ', 'Justin'),
#       ('Mike F', 'Chris'), ('Mike F', 'Joel'), ('Mike F', 'Noah'), ('Mike F', 'Cody'), ('Mike F', 'Justin'),
#       ('Chris', 'Joel'), ('Chris', 'Noah'), ('Chris', 'Cody'), ('Chris', 'Justin'), ('Joel', 'Noah'),
#       ('Joel', 'Cody'), ('Joel', 'Justin'), ('Noah', 'Cody'), ('Noah', 'Justin'), ('Cody', 'Justin')]


# house_list_current = ["James", "Mike M", "Eric", "Ben", "Roberto", "Mike F", "Chris", "Justin", "Cody", "Noah", "Joel", "Anthony"]