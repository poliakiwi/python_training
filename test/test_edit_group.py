from model.group import Group

def test_edit_first_group_name(app):
    if app.groups.count() == 0:
        app.groups.create(Group(name="Test"))
    app.groups.edit_first(Group(name="New name"))


def test_edit_first_group_header(app):
    if app.groups.count() == 0:
        app.groups.create(Group(header="Test"))
    app.groups.edit_first(Group(header="New header"))




