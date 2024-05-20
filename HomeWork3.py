dano = [[1, 2, 3], {"a": 4, "b": 5}, (6, {"cube": 7, "drum": 8}), "Hello", ((), [{(2, "Urban", ("Urban2", 35))}])]

new_list = []
def what_inside(*data_):  #  функция вывода исходных вложенных данных в список
    global new_list
    for i in data_:
        if type(i) == int or type(i) == str:
            new_list.append(i)
        elif type(i) == list or type(i) == tuple or type(i) == set:
            what_inside(*i)
        elif type(i) is dict:
            for key, value in i.items():
                new_list.append(key)
                new_list.append((value))
                continue
    return new_list

def summator(list_):  #  подсчет нужной суммы
    summ = 0
    for i in list_:
        if type(i) == int:
           summ += int(i)
        else:
            summ = summ + len(i)
    return summ

print("вывод содержимого всех символов в строку для их подсчета: \n",what_inside(dano))

print("вывод итогового результата: ",summator(new_list))




