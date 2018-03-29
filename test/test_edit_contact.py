from model.contacts import Contact

def test_edit_first_contact_name(app):
    app.contacts.edit_first(Contact(fir="changed firstname"))
