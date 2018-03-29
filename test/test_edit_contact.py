from model.contacts import Contact

def test_edit_first_contact_name(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contact(fir="Test"))
    app.contacts.edit_first(Contact(fir="changed firstname"))
