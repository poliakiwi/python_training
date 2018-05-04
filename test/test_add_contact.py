# -*- coding: utf-8 -*-
from model.contacts import Contact
import pytest
import random
import string
import re


def random_str(prefix, maxlen):
    sym = string.ascii_letters + string.digits + " "*10 #+ string.punctuation
    return prefix + "".join([random.choice(sym) for i in range(random.randrange(maxlen))])


testdata = [Contact(fir="", mid="", las="", nic="", tit="", com="", add_1="", tel_1="", tel_2="", tel_3="", tel_4="",
                    mail_1="", mail_2="", mail_3="", hom="", add_2="", hom_2="", not_2="")] + [
    Contact(fir=random_str("fir",10), mid=random_str("mid",10), las=random_str("las",10), nic=random_str("nic",10),
            tit=random_str("tit",10), com=random_str("com",10), add_1=random_str("add_1",10))
    for i in range(5)
]


@pytest.mark.parametrize("cont", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, cont):
    old_cont = app.contacts.get_list()
    # newC = Contact(fir="fir1", mid="mid1", las="las1", nic="nic1", tit="tit1", com="com1", add_1="add1",
    #                             tel_1="111", tel_2="222", tel_3="333", tel_4="444", mail_1="a1@a.ru", mail_2="a2@a.ru",
    #                             mail_3="a3@a.ru", hom="hom1.ru", add_2="add2", hom_2="hom2", not_2="not2")
    app.contacts.create(cont)
    new_cont = app.contacts.get_list()
    assert len(old_cont) + 1 == len(new_cont)
    cont.las = clear_blank(cont.las)
    cont.fir = clear_blank(cont.fir)
    cont.add_1 = clear_blank(cont.add_1)
    old_cont.append(cont)
    assert sorted(old_cont, key=Contact.id_or_max) == sorted(new_cont, key=Contact.id_or_max)


def clear_blank(s):
    s1 = re.sub(" +", " ", s)
    s1 = re.sub(" $", "", s1)
    return s1





