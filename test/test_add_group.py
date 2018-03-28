# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.groups.create(Group(name="grup1", header="h1", footer="f1"))


def test_add_empty_group(app):
    app.groups.create(Group(name="", header="", footer=""))



