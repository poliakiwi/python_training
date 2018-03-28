from model.group import Group

def test_edit_first_group_name(app):
    app.session.login(username="admin", password="secret")
    app.groups.edit_first(Group(name="New name"))
    app.session.logout()

def test_edit_first_group_header(app):
    app.session.login(username="admin", password="secret")
    app.groups.edit_first(Group(header="New header"))
    app.session.logout()



