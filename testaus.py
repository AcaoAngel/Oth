def lynda(parameter_func):
    def interior_func():
        print("summa")
        parameter_func()
        print("loppu")
    return interior_func

@lynda
def summa():
    
    print(5+9)

summa()


@lynda
def substraction():
    print(9-5)

substraction()