def test(*a,**b):
    for i in a:
        print("Печать самого параметра и его тип: ",i,type(i))
    for j, value in b.items():
        print("Печать элементов словаря: ключ ", j," его значение: ",value)

dict_ = {"a": 111,"b": 222,"c": 333}
test(11,"str",(1,2,3,4),True,dict_)
test(**dict_)

def factorial(n):  #  рекурсивная функция для вычисления факториала!
    if n != 0:
        fact = n * factorial(n-1)
    else:
        fact = 1
    return fact

n = input("введите любое целое, положительное число: ",)
if n.isdigit():
    print("Факториал введенного вами числа ",n," составляет",factorial(int(n)))
else:
    print("вы ввели не целое, положительное число!! Будьте внимательны!!")