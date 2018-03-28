from model.group import Group

def test_edit_first_group_name(app):
    app.groups.edit_first(Group(name="New name"))


def test_edit_first_group_header(app):
    app.groups.edit_first(Group(header="New header"))




