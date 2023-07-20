import os

def strip_name(str):
    res = ''
    for e in str:
        if e == '`':
            continue
        else:
            res += e
    return res

def find_diff_between_lists(list1, list2):
    diff = []
    dict = {}
    for ele in list1:
        if ele in dict:
            dict[ele] += 1
        else:
            dict[ele] = 1
    for ele in list2:
        if ele in dict:
            dict[ele] += 1
        else:
            dict[ele] = 1
    for key in dict.keys():
        if dict[key] == 1:
            diff.append(key)
    return diff

def prepare_data(path):
    f = open(path, "r")
    res = []
    for line in f:
        line = line.strip()
        if line.startswith('CREATE') or line.startswith('PRIMARY') or line.startswith('KEY') or line.startswith(')'):
            continue
        else:
            lst = line.split(' ')
            name = strip_name(lst[0])
            res.append(name)
    print("preprocess successfully, columns in ddl: " + str(res))
    return res

if __name__ == '__main__':
    dir_name = os.getcwd()
    list1 = prepare_data(dir_name + "/files/ddl1.txt")
    list2 = prepare_data(dir_name + "/files/ddl2.txt")
    diff = find_diff_between_lists(list1, list2)
    print("DDL column differences: " + str(diff))
