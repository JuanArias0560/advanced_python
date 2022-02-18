
import time


# def fibo_gen(max):
#     n1 =0 
#     n2 =1
#     counter=0
#     while counter<max:
#         if counter == 0:
#             counter +=1
#             yield n1
#         elif counter ==1:
#             counter +=1
#             yield n2 
#         else:
#             aux= n1 + n2
#             n1,n2 = n2,aux
#             counter +=1
#             yield aux
    
# if __name__=='__main__':
#     fibonaci=fibo_gen(max=5)
#     for element in fibonaci:
#         print(element)
#         time.sleep(1)

def fibo_gen(max):                          # RAR Version
    n1,n2,count=0,1,0
    while count<max:
        yield n1
        n1,n2=n2,n1+n2
        count +=1

if __name__=='__main__':
    fibonaci=fibo_gen(max=5)
    for element in fibonaci:
       print(element)
       time.sleep(1)


