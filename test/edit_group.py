
def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.groups.edit_first()
    app.session.logout()