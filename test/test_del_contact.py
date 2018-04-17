from model.contacts import Contact
from random import randrange


def test_del_some_contact(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contact(fir="Test"))
    old_cont = app.contacts.get_list()
    index = randrange(len(old_cont))
    app.contacts.del_by_index(index)
    new_cont = app.contacts.get_list()
    assert len(old_cont) - 1 == len(new_cont)
    old_cont[index:index+1] = []
    assert old_cont == new_cont
