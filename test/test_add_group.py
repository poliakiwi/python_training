# -*- coding: utf-8 -*-
from model.group import Group
import re


def test_add_group(app, db, json_groups):
    gr = json_groups
    old_groups = db.get_group_list()
    app.groups.create(gr)
    new_groups = db.get_group_list()
    # assert len(old_groups) + 1 == len(new_groups)
    # gr.name = clear_blank(gr.name)
    old_groups.append(gr)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def clear_blank(s):
    s1 = re.sub(" +", " ", s)
    s1 = re.sub(" $", "", s1)
    return s1
