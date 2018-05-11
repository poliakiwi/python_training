from model.contacts import Contact
import random
import re


def test_del_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contacts.create(Contact(fir="Test"))
    old_cont = db.get_contact_list()
    cont = random.choice(old_cont)
    app.contacts.del_by_id(cont.id)
    new_cont = db.get_contact_list()
    old_cont.remove(cont)
    assert old_cont == new_cont

    def clear_blank(s):
        s = re.sub(" +", " ", s)
        s = re.sub(" $", "", s)
        return s
    def clean(cont):
        return Contact(id=cont.id, fir=clear_blank(cont.fir), las=clear_blank(cont.las), add_1=clear_blank(cont.add_1))
    if check_ui:
        ui_list = app.contacts.get_list()
        db_list = map(clean, new_cont)
        assert sorted(db_list, key=Contact.id_or_max) == sorted(ui_list, key=Contact.id_or_max)