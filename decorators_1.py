from datetime import datetime


def execution_time(func):
    def wrapper(*args ,**kwargs):
        initial_time=datetime.now()
        func(*args,**kwargs)
        final_time=datetime.now()
        time_elapsed=final_time-initial_time
        print( str(time_elapsed.total_seconds()) + ' seconds passed')

    return wrapper

@execution_time
def randon_func():
     for _ in range (1,100000000):
        pass

@execution_time
def suma(a:int , b:int)->int:
    return a+b

@execution_time
def saludo(name='Juan'):
    print('Hi '+ name)

suma(4,4)
randon_func()
saludo('Manuel')