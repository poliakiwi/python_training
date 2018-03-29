from model.contacts import Contact

def test_del_first_contact(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contact(fir="Test"))
    app.contacts.del_first()
