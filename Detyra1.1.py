"""
Detyra 1.1  “rock paper scissors ” 
 
1. Ruani zgjedhjet ne cfaredo variable te tipit qe i kemi mesu
2. Perdorni cilindo tip te unazave qe e kemi mesu
3. Beni handle si duhet edge cases gjate zgjedhjeve

"""

import random
import time  # Per te pauzuar lojen per pak qaste gjate ekzekutimit te komandave

# Praktika-detyra_1.py simulon nje loje rock, paper, scissor

# Per te bere doren e kompjuterit te rastesishme: rock, paper ose scissor, ku rock = 1, paper = 2 dhe scissor e llogarisim si 3
ran = random.randint(1, 3)

a = True
count_pc = 0
count_player = 0

while a:
    inp = input("A doni te jeni rock, paper apo scissor:")
    if (
        (inp == "rock" and ran == 1)
        or (inp == "paper" and ran == 2)
        or (inp == "scissor" and ran == 3)
    ):
        print("Nuk ka fitues")
        time.sleep(1.5)
        print(
            "Ju keni fituar:",
            count_player,
            "herë, ndërsa kompjuteri:",
            count_pc,
            "herë",
        )
        time.sleep(1)
        a = True
    elif (
        (inp == "rock" and ran == 3)
        or (inp == "paper" and ran == 1)
        or (inp == "scissor" and ran == 2)
    ):
        print("Ju keni fituar")
        time.sleep(1.5)
        count_player += 1
        print(
            "Ju keni fituar:",
            count_player,
            "herë, ndërsa kompjuteri:",
            count_pc,
            "herë",
        )
        time.sleep(1)
        a = False
    elif (
        (inp == "rock" and ran == 2)
        or (inp == "paper" and ran == 3)
        or (inp == "scissor" and ran == 1)
    ):
        print("Ju keni humbur")
        time.sleep(1.5)
        count_pc += 1
        print(
            "Ju keni fituar:",
            count_player,
            "herë, ndërsa kompjuteri:",
            count_pc,
            "herë",
        )
        time.sleep(1)
        a = False
    else:
        print("Vetem inputet rock, paper ose scissor pranohen si valide")
        time.sleep(1)
        continue  # Nese inputi nuk eshte rock, paper ose scissor kthehu ne fillim

    b = True
    while b:
        inp2 = input("A doni te luani perseri:")
        if inp2 == "po":
            time.sleep(1)
            a = True
            b = False
            ran = random.randint(
                1, 3
            )  # Ricaktoje doren e rradhes si rock,paper apo scissor
        elif inp2 == "jo":
            a = False
            b = False
        else:
            print(
                "Vetem vlerat po ose jo mund te pranohen si valide"
            )  # Nese inputi nuk eshte po ose jo, pyesim lojtarin perseri
            time.sleep(1)
