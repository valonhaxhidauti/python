'''
Ushtrimi3:
- gjeneroni nje numer random integer nga 0-10
- Permes nje for loop me rang 1-10 dhe permes while loop ju duhet te merrni inputin e userit dhe ta krahasoni ate me numrin e gjeneruar random.
- Mund te perdorni cfaredo funksioni ose variable ndihmese qe do e beje me te lehte kalkulimin.
- Ne rast se nuk eshte ofruar asnje input. Pra input==‘’,  njoftojeni userin me mesazh perkates
- Njoftojeni userin nese ka dhene input te gabuar ose te sakte.
- Ne rastin e while loop mos perdorni break statements per te dale nga unaza.
'''

import random

numri_random = random.randint(1,10)
numri_random_str = str(numri_random)
# print(numri_random)

for i in range(10):
    inputi_i_userit = input('Shkruaj nje numer:')
    if inputi_i_userit == '':
        print('Ju lutem shkruani dicka')
    elif inputi_i_userit != numri_random_str:
        print('e pasakte')
    else:
        print('bravo')
        break