"""
Detyra 3:
1. Duke perdorur API endpoint `https://gorest.co.in/public/v1/users` merrni te gjithe userat qe ekzistojne ne kete endpoint dhe ruani ata ne tipe te dhenash qe pershtatet me se miri
2. Te dhenat e ruajtuara ruani poashtu ne nje file me emrin users.txt
3. Duke perdorur authorization token ne header 'Bearer 5b950a5d5f91434c46612d15777b9ce7ebe9ab55876dd71c4ae08abab8b49c7a':
    a. Krijoni nje te dhene te re duke perdorur post request
    b. Fshini nje user ekzistues duke perdorur delete request
    c. Modifikoni nje te dhene ekzistuese duke perdorur put ose patch request.
4. Te dhenat e modifikuara, te fshira dhe te shtuara ruani ne nje file te ri me emrin new_users.txt
5. Te dhenat e modifikuara duhet te jeni ne gjendje t'i shihni edhe nga endpointi i dhene https://gorest.co.in/public/v1/users
6. Zgjidhja eshte mire te behet duke perdorur klasa dhe requests te caktuar te behen nga metoda te veqanta
"""

import requests
import json

BASE_URL = "https://gorest.co.in/public/v1/users"
token = "5b950a5d5f91434c46612d15777b9ce7ebe9ab55876dd71c4ae08abab8b49c7a"
header = {"Authorization": "Bearer {}".format(token)}


class Requests:
    def get_req():
        return requests.get(BASE_URL)

    def del_req(user_id):
        return requests.delete("{0}/{1}".format(BASE_URL, user_id), headers=header)

    def post_req(name, email):
        return requests.post(
            BASE_URL,
            headers=header,
            data={"name": name, "email": email, "gender": "male", "status": "active"},
        )

    def put_req(user_id, name, email):
        return requests.put(
            "{0}/{1}".format(BASE_URL, user_id),
            headers=header,
            data={"name": name, "email": email, "gender": "male", "status": "active"},
        )


g_req = Requests.get_req()

files = g_req.json()

dataa = []
for item in range(0, len(files["data"])):
    dataa.append(files["data"][item])


""" I shfaqim te dhenat ne nje file users.txt"""

write_file = "users.txt"
with open(write_file, "w") as f:
    for i in range(0, len(files["data"])):
        f.write("%s\n" % json.dumps(dataa[i]))


""" Se pari e krijojme nje user permes post request """

post_rq = Requests.post_req("valon", "valon1@vv.cop")
print(post_rq.text)
print(post_rq)


""" Pastaj e updajtojme ate user permes put request"""

put_req = Requests.put_req(int(post_rq.json()["data"]["id"]), "valon", "valon2@vv.cop")

print(put_req.text)
print(put_req)

""" Ne fund e fshijme userin e krijuar permes delete request dhe shohim kodin qe na vje"""

d_req = Requests.del_req(int(post_rq.json()["data"]["id"]))
print(d_req.text)
print(d_req)

""" Ne new_users.txt shenojme userin qe eshte postuar dhe pastaj perditesuar te cilin ne api endpoint https://gorest.co.in/public/v1/users ne fund e fshijme """

write_file2 = "new_users.txt"
with open(write_file2, "w") as f:
    f.write("%s\n" % post_rq.json()["data"])
    f.write("%s\n" % put_req.json()["data"])
