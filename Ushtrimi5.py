"""
Ushtrimi5:
- Krijojeni nje liste qe do te permbaje numra, string dhe boolean values, lista duhet te kete 20 elemente
- Duke perdorur isinstance fusni secilin element ne lista perkatese te tipit te cilit i takojne
- Ne rastin e numrave, nese numri eshte me i vogel se 5 fusni ne nje liste te veqante
- Ne rastin e strings nese length i stringut eshte me i madh se 3 fusni ne nje liste te veqante
- Printojni listat e krijuara bashke me mesazhet perkatese

"""

lista = [
    1,
    2,
    True,
    4,
    False,
    6,
    8,
    51,
    True,
    "hello",
    "hi",
    "Tung",
    False,
    "Pershendetje",
    -10,
    34,
    False,
    "b",
    1500,
    True,
]

lista_string = []
lista_int = []
lista_bool = []

for element in lista:
    if isinstance(element, str):
        lista_string.append(element)
    elif isinstance(element, bool):
        lista_bool.append(element)
    else:
        lista_int.append(element)

i = 0
lista_string_2 = []
while i < len(lista_string):
    if len(lista_string[i]) > 3:
        lista_string_2.append(lista_string[i])
    i += 1

j = 0
lista_int_2 = []
while j < len(lista_int):
    if lista_int[j] > 5:
        lista_int_2.append(lista_int[j])
    j += 1


print("Lista me te gjithe elementet:", lista)
print("Vlerat e tipit string te listes fillestare:", lista_string)
print("Nga te cilat me gjatesi me te madhe se 3 shkronja jane:", lista_string_2)
print("Vlerat e tipit int te listes fillestare:", lista_int)
print("Nga te cilet me te medhenj se 3 jane:", lista_int_2)
print("Vlerat e tipit boolean te listes fillestare:", lista_bool)
