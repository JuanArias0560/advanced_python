def remove_duplicates(some_list):
    # without_duplicates=[]
    # for elemen in some_list:
    #     if elemen not in without_duplicates:
    #         without_duplicates.append(elemen)
    # return without_duplicates
    return(list(set(some_list)))

def run():

    random_list=[1,1,2,2,4]
    print(remove_duplicates(random_list))

if __name__=='__main__':
    run()