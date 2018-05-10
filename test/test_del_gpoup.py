from model.group import Group
import random
import re


def test_del_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.groups.create(Group(name="Test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.groups.del_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    def clean(group):
        group.name = re.sub(" +", " ", group.name)
        return Group(id=group.id, name=group.name.strip())
    if check_ui:
        ui_list = app.groups.get_groups_list()
        db_list = map(clean, new_groups)
        assert sorted(db_list, key=Group.id_or_max) == sorted(ui_list, key=Group.id_or_max)

