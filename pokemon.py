import os 

clear=lambda:os.system('clear')       #use of lambda for the creation of a variable that cleans the screen

def choose_pokemon(func):

    def wrapper(choose):
        
        func(choose)   
        
        if choose == 1:
            print('You choose a Charmander, is a fire type pokemon')
        elif choose == 2:
            print('You choose a Bulbasaur, is a gras type pokemon')
        elif choose == 3:
            print('You choose a Squirtle, is a water type pokemon')
        elif choose == 11:
            print('Congratulations you choose a Pikachu, is a electric type pokemon')
        else:
            print('you choosed a invalid option')
    return wrapper

def run():    
    clear()
    TYPE=""" 
        HI FRIEND, IT'S DANGEROUS TO GO ALONE, CHOOSE ONE OF THE THREE

        [1] Charmander.
        [2] Bulbasaur.
        [3] Squirtle.

        Choose Whisely!!!    
    """
    print(TYPE)
    choose=int(input('Choose one option: '))
    choose_a_pokemon(choose)
    
    

@choose_pokemon
def choose_a_pokemon(choose):    
    return choose

if __name__=='__main__':
    run()
    