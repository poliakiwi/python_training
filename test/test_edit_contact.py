from model.contacts import Contact
import random
import re
from random import randrange


def test_edit_some_contact_name(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contact(fir="Test"))
    old_cont = app.contacts.get_list()
    newC = Contact(fir="changed firstname")
    index = randrange(len(old_cont))
    # newC.id = old_cont[0].id
    # newC.las = old_cont[0].las
    app.contacts.edit_by_index(index, newC)
    new_cont = app.contacts.get_list()
    assert len(old_cont) == len(new_cont)
    old_cont[index].fir = newC.fir
    assert sorted(old_cont, key=Contact.id_or_max) == sorted(new_cont, key=Contact.id_or_max)


# def test_edit_some_contact_name(app, db, check_ui):
#     if len(db.get_contact_list()) == 0:
#         app.contacts.create(Contact(fir="Test"))
#     old_cont = db.get_contact_list()
#     newC = Contact(fir="changed firstname")
#     cont = random.choice(old_cont)
#     app.contacts.edit_by_id(cont.id, newC)
#     new_cont = db.get_contact_list()
#     old_cont.remove(cont)
#     cont.fir=newC.fir
#     old_cont.append(cont)
#     assert sorted(old_cont, key=Contact.id_or_max) == sorted(new_cont, key=Contact.id_or_max)
#
#     def clear_blank(s):
#         s = re.sub(" +", " ", s)
#         s = re.sub(" $", "", s)
#         return s
#     def clean(cont):
#         return Contact(id=cont.id, fir=clear_blank(cont.fir), las=clear_blank(cont.las), add_1=clear_blank(cont.add_1))
#     if check_ui:
#         ui_list = app.contacts.get_list()
#         db_list = map(clean, new_cont)
#         assert sorted(db_list, key=Contact.id_or_max) == sorted(ui_list, key=Contact.id_or_max)
