from model.group import Group

def test_edit_first_group_name(app):
    old_groups = app.groups.get_groups_list()
    if app.groups.count() == 0:
        app.groups.create(Group(name="Test"))
    app.groups.edit_first(Group(name="New name"))
    new_groups = app.groups.get_groups_list()
    assert len(old_groups) == len(new_groups)


def test_edit_first_group_header(app):
    old_groups = app.groups.get_groups_list()
    if app.groups.count() == 0:
        app.groups.create(Group(header="Test"))
    app.groups.edit_first(Group(header="New header"))
    new_groups = app.groups.get_groups_list()
    assert len(old_groups) == len(new_groups)




