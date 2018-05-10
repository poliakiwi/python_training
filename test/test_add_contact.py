# -*- coding: utf-8 -*-
from model.contacts import Contact
import re


def test_add_contact(app, json_contacts):
    cont = json_contacts
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





