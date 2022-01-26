"""
Ushtrimi4:
- krijojeni nje liste me 10 elemente me numrat nga 1 deri ne 10
- Krijojini dy lista te zbrazta njera me emrin numrat_cift=[] dhe tjetra me emrin numrat_tek=[].
- Duke perdorur for loops, fusni numrat nga lista 10 elementeshe neper listat perkatese per numrat cift ose tek.
- Konfirmojeni duke printuar te dy listat ne fund

"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numrat_cift = []
numrat_tek = []

for elem in lista:
    if elem % 2 == 0:
        numrat_cift.append(elem)
    else:
        numrat_tek.append(elem)

print("Numrat tek nga lista me 10 numra:", numrat_tek)
print("Numrat çift nga lista me 10 numra:", numrat_cift)
