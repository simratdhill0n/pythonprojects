from random import randint
ran_num= randint(1,101)
ls=[]
game= True
while game:
    pick= input('Enter a number between 1 to 100: ')
    if pick.isdigit():
        if int(pick) in list(range(1,101)):
            ls.append(int(pick))
            if len(ls)==1:
                if abs(ran_num-int(pick))<=10:
                    print('WARM')
                else:
                    print('COLD')
            else:
                if int(pick)==ran_num:
                    print(f'Correct, in {len(ls)} tries')
                    game=False
                    break
                elif abs(ran_num-ls[len(ls)-1])<abs(ran_num-ls[len(ls)-2]):
                    print('WARMER')
                    
                else:
                    print('COLDER')
        else:
            print('OUT OF BOUNDS')
    else:
        print('Input is not an Interger')
    