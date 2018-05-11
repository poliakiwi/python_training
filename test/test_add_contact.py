# -*- coding: utf-8 -*-
from model.contacts import Contact
import re


def test_add_contact(app, db, check_ui, json_contacts):
    cont = json_contacts
    old_cont = db.get_contact_list()
    app.contacts.create(cont)
    new_cont = db.get_contact_list()
    old_cont.append(cont)
    assert sorted(old_cont, key=Contact.id_or_max) == sorted(new_cont, key=Contact.id_or_max)

    def clear_blank(s):
        s = re.sub(" +", " ", s)
        s = re.sub(" $", "", s)
        return s
    def clean(cont):
        return Contact(id=cont.id, fir=clear_blank(cont.fir.strip()), las=clear_blank(cont.las.strip()), add_1=clear_blank(cont.add_1.strip()))
    if check_ui:
        ui_list = app.contacts.get_list()
        db_list = map(clean, new_cont)
        assert sorted(db_list, key=Contact.id_or_max) == sorted(ui_list, key=Contact.id_or_max)
