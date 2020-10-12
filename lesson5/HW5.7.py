import json

def read_file():
    with open('HW5.7.txt', 'r', encoding='utf-8') as a:
        file_text = a.readlines()
    return file_text

def average_func():
    summ_profit = 0
    count = 0
    for i in read_file():
        i = i.split()
        profit = int(i[2]) - int(i[3])
        if profit > 0:
            summ_profit = summ_profit + profit
            count += 1
    return {'average_profit': summ_profit / count}

def profits():
    profits_dict = dict()
    for i in read_file():
        i = i.split()
        profit = int(i[2]) - int(i[3])
        profits_dict.update({i[0]: profit})
    return profits_dict

with open('HW5.7.json', 'w') as a:
    finished_list = [profits(), average_func()]
    json.dump(finished_list, a)


