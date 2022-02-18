
def PrimeNumber(numb: int):
    check_numb=[values for values in range(2,numb+1)if numb% values==0]
    veri_numb= len(check_numb)==1
    if veri_numb==True:
        print('is a prime number')
    else:
        print('is not a prime number')


def run():
    numb: int =int(input("type a number: "))

    if numb >=1:
        PrimeNumber(numb)
    else: 
        print('Chose a number greather than 1 ')



if __name__=='__main__':
    run()