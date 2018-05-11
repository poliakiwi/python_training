# -*- coding: utf-8 -*-
from model.group import Group
import re


def test_add_group(app, db, check_ui, json_groups):
    gr = json_groups
    old_groups = db.get_group_list()
    app.groups.create(gr)
    new_groups = db.get_group_list()
    old_groups.append(gr)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

    def clean(group):
        group.name = re.sub(" +", " ", group.name)
        return Group(id=group.id, name=group.name.strip())
    if check_ui:
        ui_list = app.groups.get_groups_list()
        db_list = map(clean, new_groups)
        assert sorted(db_list, key=Group.id_or_max) == sorted(ui_list, key=Group.id_or_max)


