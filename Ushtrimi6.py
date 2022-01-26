""" Ushtrimi6.py
- krijoni nje funksion qe pret nje parameter url dhe qe e performon nje get request ne ate url
- krijojeni nie funksion qe pret nje parameter url dhe qe e performon nje post request ne ate url
- krijoni nje funksion qe pret nje parameter url dhe performon nje delete request ne ate url
- krijojeni nje funksion qe pret nje parameter number dhe qe e kthen nje variabel te tipit string qe do te marre vleren “get” nese numri eshte 1, “post” nese numri eshte 2 dhe “delete” nese numri eshte 3
- jashte cdo funksioni mundesoni userit te jape inputin e tij dhe kthejeni ate input ne integer duke e futur ne bllok try/except nese useri ka futur shkronja e jo numra
- inputin e userit bejani pass funksionit qe pret numer dhe varesisht nga vlera qe kthehet nga ai funksion bejeni run funksionin me requestin e duhur
"""
import requests


def get_req(url):
    print(requests.get(url))


def post_req(url):
    print(requests.post(url))


def delete_req(url):
    print(requests.delete(url))


def which_method(numri):
    inst = isinstance(numri, int)
    while inst:
        if numri == 1:
            r = get_req("https://google.com")
            inst = False
        elif numri == 2:
            r = post_req("https://google.com")
            inst = False
        elif numri == 3:
            r = delete_req("https://google.com")
            inst = False
        else:
            r = 0
            inst = False
    return r


a = True
while a:
    try:
        user_input = int(input("Shkruaj nje numer:"))
        if 1 <= user_input <= 3:
            metoda = which_method(user_input)
            a = False
        else:
            print("shkruani numer nga 1 deri ne 3:")
    except ValueError as err:
        print("This is not an integer number. Please enter a valid number.", err)
