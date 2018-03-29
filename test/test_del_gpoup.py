from model.group import Group

def test_del_first_group(app):
    if app.groups.count() == 0:
        app.groups.create(Group(name="Test"))
    app.groups.del_first()
