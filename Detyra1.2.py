'''
Detyra 1.2 Qello numrin random treshifror

1. Gjeneroni nje numer random tre shifror
2 mundesoni userit te bej tre inputa dhe krahasoni ata inputa me numrin e gjeneruar 
3. Perdorni te dyjat for loop dhe while loop per ta zgjidhur detyren
4. Bejini handle si duhet edge cases
5. Useri mund te bej input vetem numra nje shifror

'''

import random
import time

# rand gjeneron nje numer treshifror
rand = str(random.randint(100,999)) 

a = True
result = []
A = 1
count = 0
# while loop i pare na tregon sa numra kemi qelluar
while a:
    # for loop i pare e kthen numri treshifrore ne nje liste me 3 elemente te tipit int
    for i in range(0, len(rand), A):
        result.append(int(rand[i : i + A]))
    # for loop i dyte kerkon si inpute 3 numra nje-shifror  
    for i in range(3):
        user = input('Shkruaj një numer 1 shifror:')
        try:
            if int(user) in result:            
                count += 1
                print('Ke qelluar', count)
                time.sleep(1)
            else:
                print(user,'nuk ben pjese ne numrin treshifror')
                time.sleep(1)
        except ValueError as err:
            print('Vetem integer pranohen si input:',err)
            continue
    if count == 0:
        print('Ju nuk keni qelluar asnje numer')
        time.sleep(1)
    elif count == 1:
        print('Ju keni qelluar 1 numer')
        time.sleep(1)
    elif count == 2:
        print('Ju keni qelluar 2 numra')
        time.sleep(1)
    else:
        print('Ju keni qelluar 3 numrat nga numri treshifror, Bravo!')
        time.sleep(1)
    print('Numri ishte',rand)
    time.sleep(1)
    b = True
    # while loop i dyte na pyet nese duam te luajme serish ose jo
    while b:
        user1 = input('Doni te provoni serish:')
        if user1 == 'po':
            # ricaktojme numrin treshifror nese useri don te luaje serish
            rand = str(random.randint(100,999))
            count = 0 
            result = []
            b = False
            time.sleep(1)
        elif user1 == 'jo':
            a = False
            b = False
        else:
            print('Vetem opsionet po ose jo pranohen si inpute')
            time.sleep(1)
               

