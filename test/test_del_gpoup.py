from model.group import Group

def test_del_first_group(app):
    app.session.login(username="admin", password="secret")
    app.groups.del_first()
    app.session.logout()