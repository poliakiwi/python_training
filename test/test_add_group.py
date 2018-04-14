# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups = app.groups.get_groups_list()
    app.groups.create(Group(name="grup1", header="h1", footer="f1"))
    new_groups = app.groups.get_groups_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_add_empty_group(app):
    old_groups = app.groups.get_groups_list()
    app.groups.create(Group(name="", header="", footer=""))
    new_groups = app.groups.get_groups_list()
    assert len(old_groups) + 1 == len(new_groups)



