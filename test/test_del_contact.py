from model.contacts import Contact

def test_del_first_contact(app):
    app.contacts.del_first()
