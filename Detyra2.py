"""
Detyra 2:

1. Create a class called CurrencyConverter
2. Create a method to register users with passwords- password need to have at least 1 number and one uppercase letter
3. Create two users using the above method, and allow only one of them to be admin
4. Create a method that will make the conversion from eur to usd by accepting an input which can be int or float
5. Create a method that will change the way we convert eur to usd (it can be just a dumb calculation) 
6. Allow only admin user to make changes to this function
7. After admin changes the code needs to use the new method to convert money.

"""

import re
import os


class CurrencyConverter:

    conversion_rate = 1.1  # Norma e konvertimit euro ne dollare eshte ~ 1.1

    def __init__(self, user, password, admin):
        self.admin = admin
        self.user = user
        self.password = password

    # Kjo metode kthen passwordin e userit
    def get_pass(self):
        return self.password

    # Kjo metode kontrollon nese passwordi eshte te pakten me nje shkronje te vogel, nje te madhe, nje numer dhe me shume se 8 shkronja i gjate
    def check_password(self, password):

        flag = 0
        if not re.search("[a-z]", password):
            flag = 1
        if not re.search("[0-9]", password):
            flag = 1
        if not re.search("[A-Z]", password):
            flag = 1
        if len(password) < 8:
            flag = 1
        if flag != 0:
            raise Exception("Paswordi eshte jo valid")

    # Kjo metode kthen eurot ne dollare me nje norme te caktuar qe mirret si baze 1.1
    def convert_eur_usd(self, euro):
        return euro * self.conversion_rate

    # Kjo metode lejon ndrrimin e normes se konvertimit vetem nese useri eshte admin
    def set_admin_convertion(self, rate):
        if self.admin == False:
            raise Exception("Nuk jeni admin")
        self.conversion_rate = rate

    # Kjo metode lejon konvertimin me norme te re nese useri thjesht e din passwordin e userit admin
    def set_admin_convertion_withPass(self, rate, password, user_admin):
        if user_admin.get_pass() != password:
            raise Exception(
                "Nuk mund ta qasni metoden e re te konvertimit pasi keni dhene gabim passowrdin e adminit"
            )
        self.conversion_rate = rate


# testing code
user1 = "valon_admin"
password1 = input("Passwordi i userit admin:")
user2 = "valon_user"
password2 = input("Passwordi i userit normal:")

# Inicializojme nje user admin
user_admin = CurrencyConverter(user1, password1, True)
# Inicializojme nje user normal
user_normal = CurrencyConverter(user2, password2, False)

try:
    user_admin.check_password(password1)
except Exception as ex:
    print(ex, "per userin e pare")
    os._exit(0)


try:
    user_normal.check_password(password2)
except Exception as ex:
    print(ex, "per userin e dyte")
    os._exit(0)


euro = input("Sa euro doni ti konvertoni ne dollar:")
euro_convert_first = user_admin.convert_eur_usd(float(euro))
print(
    euro,
    "euro me konvertimin nga useri admin me metoden e pare:",
    euro_convert_first,
    "dollare",
)

euro_convert_first_user = user_normal.convert_eur_usd(float(euro))
print(
    "Konvertimi i njejte nga nje user normal me metoden e pare:",
    euro_convert_first_user,
    "dollare",
)

rate = input("Sa doni qe te jete norma e re e konvertimit:")
user_admin.set_admin_convertion(float(rate))
euro_convert_second = user_admin.convert_eur_usd(float(euro))
print(
    euro, "euro me konvertimin e metodes se dyte jane:", euro_convert_second, "dollare"
)


try:
    # Tentojme te bejme nje konvertim me nje norme(ne kete rast 3) nga nje user i thjeshte
    user_normal.set_admin_convertion(3)
    euro_convert_second_user = user_normal.convert_eur_usd(float(euro))
    # Kjo linje nuk printohet kurre pasi qe useri normal nuk ka qasje ne metoden e dyte
    print("Konvertimi i userit normal:", euro_convert_second_user, "dollare")
except Exception as ex:
    print("Konvertimi me metoden e dyte nga nje user normal nuk ben pasi qe ju,", ex)

try:
    rate = input("Sa doni qe te jete norma e re e konvertimit:")
    admin_password = input("Shkruani passwordin e adminit:")
    user_normal.set_admin_convertion_withPass(float(rate), admin_password, user_admin)
    # Bejme konvertimin e ri te eurove nga nje user i thjeshte me norme te re
    euro_third = user_normal.convert_eur_usd(float(euro))
    print(
        "Konvertimi i ri me norme",
        rate,
        "i",
        euro,
        "eurove eshte:",
        euro_third,
        "dollare",
    )
except Exception as ex:
    print(ex)
