from model.contacts import Contact
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