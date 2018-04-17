from model.group import Group

def test_del_first_group(app):
    if app.groups.count() == 0:
        app.groups.create(Group(name="Test"))
    old_groups = app.groups.get_groups_list()
    app.groups.del_first()
    new_groups = app.groups.get_groups_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups
