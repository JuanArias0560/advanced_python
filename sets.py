

def union(a,b):
    myset= a|b
    print(myset)

def intersection(a,b):
    myset= a&b
    print(myset)

def dife(a,b):
    my_set=a-b
    my_set1=b-a
    print( my_set,my_set1)

def difeSet(a,b):
    myset= a^b
    print(myset)

if __name__=='__main__':
    myset1={'juan','manuel','arias'}
    myset2={'manuel','arias','saldaña'}

    union(myset1,myset2)
    intersection(myset1,myset2)
    dife(myset1,myset2)
    difeSet(myset1,myset2)

