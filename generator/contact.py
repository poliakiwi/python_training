# -*- coding: utf-8 -*-
from model.contacts import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number contact", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_str(prefix, maxlen):
    sym = string.ascii_letters + string.digits + " "*10 #+ string.punctuation
    return prefix + "".join([random.choice(sym) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(fir="", mid="", las="", nic="", tit="", com="", add_1="", tel_1="", tel_2="", tel_3="", tel_4="",
            mail_1="", mail_2="", mail_3="", hom="", add_2="", hom_2="", not_2="")] + [
    Contact(fir=random_str("fir",10), mid=random_str("mid",10), las=random_str("las",10), nic=random_str("nic",10),
            tit=random_str("tit",10), com=random_str("com",10), add_1=random_str("add_1",10))
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)


with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
