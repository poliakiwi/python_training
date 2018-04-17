from model.group import Group
from random import randrange

def test_del_some_group(app):
    if app.groups.count() == 0:
        app.groups.create(Group(name="Test"))
    old_groups = app.groups.get_groups_list()
    index = randrange(len(old_groups))
    app.groups.del_group_by_index(index)
    new_groups = app.groups.get_groups_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[index:index+1] = []
    assert old_groups == new_groups
