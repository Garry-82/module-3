def test ():
    a = "local 1"
    b = "local 2"
    print(a,b)
test()

def test2 (a,b,c=333):
    a = "local info!!!"
    print("печать параметра, определяемого локально, в функции: ",a)
    print("печать присвоеного параметра: ",b)
    print("печать заданного функции параметра: ",c)
test2(a=111,b=222)