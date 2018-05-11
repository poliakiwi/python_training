from model.group import Group
import random
import re

def test_edit_group_name_by_index(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.groups.create(Group(name="Test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    newG = Group(name="New name")
    newG.id = group.id
    app.groups.edit_by_id(group.id, newG)
    new_groups = db.get_group_list()
    old_groups.remove(group)
    old_groups.append(newG)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

    def clean(group):
        group.name = re.sub(" +", " ", group.name)
        return Group(id=group.id, name=group.name.strip())
    if check_ui:
        ui_list = app.groups.get_groups_list()
        db_list = map(clean, new_groups)
        assert sorted(db_list, key=Group.id_or_max) == sorted(ui_list, key=Group.id_or_max)
