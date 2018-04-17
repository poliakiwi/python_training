from model.contacts import Contact


def test_del_first_contact(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contact(fir="Test"))
    old_cont = app.contacts.get_list()
    app.contacts.del_first()
    new_cont = app.contacts.get_list()
    assert len(old_cont) - 1 == len(new_cont)
    old_cont[0:1] = []
    assert old_cont == new_cont
