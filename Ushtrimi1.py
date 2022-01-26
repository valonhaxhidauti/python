"""
Ushtrimi1
"""

# Stringjet:
teksti = "Kjo eshte nje detyre me stringje"

# 1. Ndajeni secilen fjale te variables teksti ne nje liste dhe printojeni ate liste.
s = teksti.split()
print(s)

# 2. Printojeni variablen lower_case_text duke zevendesuar shkronjen e pare me shkronje te madhe?
lower_case_text = "shkronja"
print(lower_case_text.capitalize())

# 3. Printojini tre elementet e para te variables teksti.
print(s[:3])
# 4. Printojeni vetem fjalen "detyre" nga variabla teksti.
print(s[3])

# 5. Keni nje variables a='mate' dhe b='matika' , cfare operatori do te perdorni per te krijuar nje variabel c='matematika'
a = "mate"
b = "matika"
c = a + b
# print(c)

# Listat:
lista_ime = [1, 2, 3, 4, 1, 2, True, False, "test", "test", "test", "emri"]

# 1. printojeni gjatesine e listes.
print(len(lista_ime))

# 2. Perditesojeni listen me emrin tuaj.
lista_ime[11] = "Valon"

# 3. Shtojani listes elementet e lista2=['mbiemri','mosha']
lista2 = ["mbiemri", "mosha"]
lista_ime.extend(lista2)
# print(lista_ime)

# 4. Hiqini duplicates nga lista
print(set(lista_ime))

# Tuples:

# 1. Shkruajeni nje tuple qe perbehet nga nje element i vetem
tple = ("valon",)

# 2. Variablen e tipit tuple konfirmojeni qe i takon tipit tuple duke printuar tipin e variables.
print(type(tple))

# Dicts:

# 1. Krijoni nje variabel te tipit dict ku do ruani keys: emri, mbiemri, mosha
my_dict = {"emri": "valon", "mbiemri": "haxhidauti", "mosha": 24}

# 2. Variables shtojani key-n "numri_i_telefonit" dhe ruajeni vleren e telefonit tuaj
nr_tel = {"numri_i_telefonit": "045-336-084"}
my_dict.update(nr_tel)

# 3. Konfirmojeni qe e keni update-uar variablen duke e printu serish.
print(my_dict)

# 4. Nga dict i krijuar printojini vetem keys
print(my_dict.keys())

# 5. Nga dict i krijuar printojini vetem values
print(my_dict.values())

# 6. Krijoni nje dictionary te ri duke perdorur keys nga dictionary paraprak, values per kete dictionary te ri le te jene te gjitha True.
new_my_dict = dict.fromkeys(my_dict, True)
print(new_my_dict)
