from model.group import Group

def test_edit_first_group_name(app):
    old_groups = app.groups.get_groups_list()
    if app.groups.count() == 0:
        app.groups.create(Group(name="Test"))
    newG = Group(name="New name")
    newG.id = old_groups[0].id
    app.groups.edit_first(newG)
    new_groups = app.groups.get_groups_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = newG
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_edit_first_group_header(app):
#     old_groups = app.groups.get_groups_list()
#     if app.groups.count() == 0:
#         app.groups.create(Group(header="Test"))
#     app.groups.edit_first(Group(header="New header"))
#     new_groups = app.groups.get_groups_list()
#     assert len(old_groups) == len(new_groups)




