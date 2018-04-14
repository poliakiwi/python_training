# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups = app.groups.get_groups_list()
    newG = Group(name="grup1", header="h1", footer="f1")
    app.groups.create(newG)
    new_groups = app.groups.get_groups_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(newG)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_empty_group(app):
    old_groups = app.groups.get_groups_list()
    newG=Group(name="", header="", footer="")
    app.groups.create(newG)
    new_groups = app.groups.get_groups_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(newG)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



