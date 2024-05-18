def print_param(a=1, b="abcdef", c=[1, 2, 3, 4, 5]):
    print("--------------------------------------------")
    print("печать объектов поэлементно: ", a, b, c)
    print("печать объектов поэлементно с распаковкой! ", a, *b, *c)


print("вывод исходных, по умолчанию заданных параметров функции: ")
print_param()
print_param(22, "new")
print_param(True, "ssss", "3333")
print_param(c=[3, 3, 3, 3, 3])

value_list = ["aaa", [2, 2, 2, 2], [3,3,3,3]]
value_dict = {"a": True,"b": "bbb","c": [3, 3, 3]}

print("Передача распакованных элементов Списка в параметры функции:  ")
print_param(*value_list)
print_param(**value_dict)

value_list2 = [222,"---Список2---"]
print("проверка работы функции со списком из двух элементов и присвоенным параметром")
print_param(*value_list2, "ccc")
