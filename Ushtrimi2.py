"""
Ushtrimi2:
- krijojeni nje liste me 10 elemente te tipit: int, str dhe boolean
- printoni elementin e pare te listes
- printoni elementin e fundit te listes
- printoni tre elementet e para
- printoni tre elementet e fundit
- printoni elementin e katert te listes
- largojini nga lista elementet qe perseriten(duke perdorur set)

"""

lista1 = [4, 4, True, 7, "Emri", "Mbiemri", True, 42, False, "s"]


ln = len(lista1)

print("ky eshte elementi i pare:", lista1[0])

# print(lista1[-1:])
print("ky eshte elementi i fundit:", lista1[ln - 1 :])
print("keto jane tre elementet e para:", lista1[:3])

# print(lista1[-3:])
print("keto jane tre elementet e fundit:", lista1[ln - 3 :])
print("ky eshte elementi i katert:", lista1[3])


grupimi = set(lista1)
print("lista pas grupimit te elementeve:", grupimi)
