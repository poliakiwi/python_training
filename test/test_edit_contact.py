from model.contacts import Contact

def test_edit_first_contact_name(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contact(fir="Test"))
    old_cont = app.contacts.get_list()
    newC = Contact(fir="changed firstname")
    # newC.id = old_cont[0].id
    # newC.las = old_cont[0].las
    app.contacts.edit_first(newC)
    new_cont = app.contacts.get_list()
    assert len(old_cont) == len(new_cont)
    old_cont[0].fir = newC.fir
    assert sorted(old_cont, key=Contact.id_or_max) == sorted(new_cont, key=Contact.id_or_max)